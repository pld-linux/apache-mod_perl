%include	/usr/lib/rpm/macros.perl
Summary:	A Perl interpreter for the Apache Web server
Summary(pl):	Interpreter perla dla serwera WWW Apache
Name:		apache-mod_perl
Version:	1.25
Release:	4
License:	GPL
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery
Source0:	http://perl.apache.org/dist/mod_perl-%{version}.tar.gz
Patch0:		apache-perl-rh.patch
# from ftp://ftp.kddlabs.co.jp/Linux/packages/Kondara/pub/Jirai/
Patch1:		mod_perl-v6.patch
BuildRequires:	apache(EAPI)-devel
BuildRequires:	gdbm-devel
BuildRequires:	perl >= 5.6.1
BuildRequires:	perl-B-Graph
BuildRequires:	perl-BSD-Resource
BuildRequires:	perl-Devel-Symdump
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-MIME-Base64
BuildRequires:	perl-URI
BuildRequires:	perl-libwww
BuildRequires:	rpm-perlprov >= 3.0.3-16
Prereq:		apache(EAPI)
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
	WITH_APXS=/usr/sbin/apxs \
	EVERYTHING=1 \
	PERL_STACKED_HANDLERS=1

(cd apaci; ln -s ../src/modules .; chmod +x find_source)
%{__make}

(cd faq; make)

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/apache,/home/httpd/manual/mod}

%{__make} pure_install DESTDIR=$RPM_BUILD_ROOT
	
install apaci/libperl.so $RPM_BUILD_ROOT%{_libdir}/apache
install htdocs/manual/mod/mod_perl.html \
	$RPM_BUILD_ROOT/home/httpd/manual/mod

gzip -9nf README INSTALL ToDo

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/apxs -e -a -n perl %{_libexecdir}/libperl.so 1>&2
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
fi

%preun
if [ "$1" = "0" ]; then
	/usr/sbin/apxs -e -A -n perl %{_libexecdir}/libperl.so 1>&2
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd stop 1>&2
	fi
fi


%files
%defattr(644,root,root,755)
%doc *.gz faq/*.html apache-modlist.html eg
%doc /home/httpd/manual/mod/*html

%attr(755,root,root) %{_libdir}/apache/*.so

%{perl_sitearch}/*.pm
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
