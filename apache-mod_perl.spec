%include	/usr/lib/rpm/macros.perl
Summary:	A Perl interpreter for the Apache Web server
Summary(pl):	Interpreter perla dla serwera WWW Apache
Name:		apache-mod_perl
Version:	1.25
Release:	2
License:	GPL
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Source0:	http://perl.apache.org/dist/mod_perl-%{version}.tar.gz
Patch0:		apache-perl-rh.patch
# from ftp://ftp.kddlabs.co.jp/Linux/packages/Kondara/pub/Jirai/
Patch1:		mod_perl-v6.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	apache-devel
BuildRequires:	gdbm-devel
BuildRequires:	perl-libwww
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-MIME-Base64
BuildRequires:	perl-BSD-Resource
BuildRequires:	perl-B-Graph
BuildRequires:	perl-Devel-Symdump
BuildRequires:	perl-URI
Requires:	apache
Provides:	perl(mod_perl_hooks)
Provides:	mod_perl
Obsoletes:	mod_perl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mod_perl incorporates a Perl interpreter into the Apache web server,
so that the Apache web server can directly execute Perl code. Mod_perl
links the Perl runtime library into the Apache web server and provides
an object-oriented Perl interface for Apache's C language API. The end
result is a quicker CGI script turnaround process, since no external
Perl interpreter has to be started.

%description -l pl
Mod_perl jest modu³em, który wyposa¿a serwer Apache w interpreter
perla, umo¿liwiaj±c w ten sposób bezpo¶rednie wykonywanie kodu perla
przez serwer bez potrzeby anga¿owania zewnêtrznego interpretera, co
przyspiesza procesy zwi±zane z uruchamianiem skryptów CGI.

%prep
%setup  -q -n mod_perl-%{version}
%patch0 -p1
%patch1 -p1

%build
perl Makefile.PL \
	USE_APXS=1 \
	WITH_APXS=%{_sbindir}/apxs \
	EVERYTHING=1 \
	PERL_STACKED_HANDLERS=1

(cd apaci; ln -s ../src/modules .; chmod +x find_source)
%{__make}

(cd faq; make)

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/apache,/home/httpd/html/manual/mod}

%{__make} pure_install DESTDIR=$RPM_BUILD_ROOT
	
install -m 755 apaci/libperl.so $RPM_BUILD_ROOT%{_libdir}/apache
install htdocs/manual/mod/mod_perl.html \
	$RPM_BUILD_ROOT/home/httpd/html/manual/mod

find $RPM_BUILD_ROOT -name \*.so -exec strip --strip-unneeded {} \;

(
	cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/mod_perl/
	mv .packlist .packlist.old
	sed -e "s|$RPM_BUILD_ROOT||g" < .packlist.old > .packlist
	rm -f .packlist.old
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README INSTALL ToDo

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/apxs -e -a -n perl %{_libexecdir}/libperl.so 1>&2
if [ -f /var/lock/subsys/httpd ]; then
   /etc/rc.d/init.d/httpd restart 1>&2
fi

%preun
%{_sbindir}/apxs -e -A -n perl %{_libexecdir}/libperl.so 1>&2

if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd stop 1>&2
fi


%files
%defattr(644,root,root,755)
%doc {README,INSTALL,ToDo}.gz faq/*.html apache-modlist.html eg
%doc /home/httpd/html/manual/mod/*html

%attr(755,root,root) %{_libdir}/apache/*.so

%{perl_sitearch}/*.pm
%{perl_sitearch}/*.pod
%{perl_sitearch}/*.PL

%{perl_sitearch}/Apache/*.pm
%{perl_sitearch}/Apache/Constants
%{perl_sitearch}/Bundle/*.pm
%{perl_sitearch}/auto/mod_perl
%dir %{perl_sitearch}/auto/Apache/Leak
%dir %{perl_sitearch}/auto/Apache/Symbol

%{perl_sitearch}/auto/*/*/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/*/*/*.so

%{_mandir}/man3/*
