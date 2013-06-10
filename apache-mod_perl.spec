# TODO:
# - separate devel things from runtime things (apache-mod_perl-2.0.2-2 marks perl-ExtUtils-MakeMaker-6.25_08-1 (cap perl(ExtUtils::Install)))
#
# Conditional build:
%bcond_without	autodeps	# don't care about perl() deps resolving
%bcond_with	tests		# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		apxs	/usr/sbin/apxs
%define		mod_name	perl

%define		ver	2.0.7
%define		snap	svn1448242
%define		rel	6
Summary:	A Perl interpreter for the Apache Web server
Summary(cs.UTF-8):	Vestavěný interpret Perlu pro WWW server Apache
Summary(da.UTF-8):	En indbygget Perl-fortolker for webtjeneren Apache
Summary(de.UTF-8):	Ein eingebetteter Perl-Interpreter für den Apache Web-Server
Summary(es.UTF-8):	Intérprete Perl para el servidor Web Apache
Summary(fr.UTF-8):	Interpréteur Perl intégré pour le serveur Web Apache
Summary(id.UTF-8):	Interpreter Perl untuk web server Apache
Summary(is.UTF-8):	Perl túlkur fyrir Apache vefþjóninn
Summary(it.UTF-8):	Interprete Perl integrato per il server Web Apache
Summary(ja.UTF-8):	Apache Web サーバー用の組込み Perl インタープリタ
Summary(nb.UTF-8):	En Perl-fortolker for webtjeneren Apache
Summary(pl.UTF-8):	Interpreter Perla dla serwera WWW Apache
Summary(pt.UTF-8):	Um interpretador de Perl embebido para o servidor Web Apache
Summary(ru.UTF-8):	Встроенный интерпретатор Perl для WWW-сервера Apache
Summary(sk.UTF-8):	Interpreter jazyka Perl pre webový server Apache
Summary(sl.UTF-8):	Vključeni perlovski tolmač za spletni strežnik Apache
Summary(sv.UTF-8):	En inbyggd Perl-interpretator för webbservern Apache
Summary(uk.UTF-8):	Модуль вбудовування інтерпретатора Perl в сервер Apache
Summary(zh_CN.UTF-8):	用于 Apache web 服务程序的 Perl 解释程序。
Name:		apache-mod_perl
Version:	%{ver}
Release:	0.%{snap}.%{rel}
Epoch:		1
License:	Apache
Group:		Networking/Daemons/HTTP
#Source0:	http://perl.apache.org/dist/mod_perl-%{version}.tar.gz
# svn export -r 1448242 https://svn.apache.org/repos/asf/perl/modperl/branches/httpd24 mod_perl-2.0.7-svn1448242
# tar czvf mod_perl-2.0.7-svn1448242.tar.gz mod_perl-2.0.7-svn1448242
Source0:	mod_perl-%{version}-%{snap}.tar.gz
# Source0-md5:	8b62bbfe8b499bc87b6d3d28eb765a24
Source1:	%{name}.conf
Patch0:		%{name}-Makefile_PL.patch
Patch1:		perl-5.18.patch
URL:		http://perl.apache.org/
BuildRequires:	apache-devel >= 2.0.55-1
BuildRequires:	apr-util-devel >= 1:1.0.0
BuildRequires:	expat-devel
BuildRequires:	gdbm-devel
BuildRequires:	openldap-devel >= 2.4.6
%{?with_autodeps:BuildRequires:	perl-Data-Flow}
BuildRequires:	perl-devel >= 1:5.18.0
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	rpmbuild(macros) >= 1.268
%if %{with tests}
BuildRequires:	apache-mod_auth_basic
BuildRequires:	apache-mod_authz_host
BuildRequires:	apache-mod_deflate
BuildRequires:	apache-mod_env
BuildRequires:	apache-mod_include
BuildRequires:	apache-mod_mime
BuildRequires:	apache-mod_proxy
BuildRequires:	perl-CGI >= 3.22
%endif
# older apache-mod_perl could make bad autodeps to perl-mod_perl
BuildConflicts:	apache-mod_perl < 1:2.0.2-9
Requires:	apache(modules-api) = %apache_modules_api
Requires:	perl-mod_%{mod_name} = %{epoch}:%{version}-%{release}
Provides:	apache(mod_perl)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# TODO: separate -devel with ExtUtils::Embed and friends?
%define		_noautoreq	'perl(Apache::.*)' 'perl(mod_perl)' 'perl(ModPerl::.*)' 'perl(ExtUtils::Embed)' 'perl(Module::Build)'
%define		apacheconfdir	%(%{apxs} -q SYSCONFDIR 2>/dev/null)/conf.d
%define		apachelibdir	%(%{apxs} -q LIBEXECDIR 2>/dev/null)

%description
Mod_perl incorporates a Perl interpreter into the Apache web server,
so that the Apache web server can directly execute Perl code. Mod_perl
links the Perl runtime library into the Apache web server and provides
an object-oriented Perl interface for Apache's C language API. The end
result is a quicker CGI script turnaround process, since no external
Perl interpreter has to be started.

%description -l cs.UTF-8
Modul mod_perl začleňuje interpret Perlu do WWW serveru Apache, takže
WWW server může přímo provádět programy v Perlu. Mod_perl připojuje
běhovou knihovnu Perlu do Apache WWW serveru a poskytuje objektově
orientované perlovské rozhraní pro API serveru Apache. Výsledkem je
rychlejší start CGI skriptů, protože nemusí být startován externí
interpret Perlu.

%description -l de.UTF-8
Mod_perl integriert einen Perl-Interpreter in den Apache Web-Server,
so dass dieser Perl-Code direkt ausführen kann. Das Programm verknüpft
die Perl-Runtime-Bibliothek mit dem Apache Web-Sever und stellt eine
objektorientierte Perl-Benutzeroberfläche für die C-API des
Apache-Servers bereit. Das Resultat ist eine schnellere Ausführung von
CGI-Skripten, da kein externer Perl-Interpreter gestartet werden muss.

%description -l es.UTF-8
Mod_perl incluye un intérprete Perl en el servidor Apache, de manera
que se puede ejecutar el código Perl directamente desde el servidor
Web. Mod_perl enumera las bibliotecas runtime del Perl al Web servidor
Apache y proporciona una interfaz Perl object-oriented para las API
del lenguaje C. De tal modo que se obtiene una ejecución más rápida de
los script CGI sin necesidad de apoyarse en un intérprete Perl.

%description -l fr.UTF-8
Mod_perl incorpore un interpréteur Perl dans le serveur Web Apache, de
manière à ce que le serveur Web Apache puisse exécuter directement du
code Perl. Mod_perl lie la bibliothèque d'exécution Perl au serveur
Web Apache et fournit une interface Perl orientée objet pour l'API en
langage C d'Apache. Le résultat final est une exécution des scripts
CGI plus rapide, du fait qu'aucun interpréteur Perl externe ne doit
être démarré.

%description -l id.UTF-8
Mod_perl memasukkan interpreter Perl ke dalam web server Apache,
sehingga Apache dapat secara langsung menjalankan kode Perl. Mod_perl
me-link runtime library Perl ke dalam web server Apache dan
menyediakan antarmuka Perl yang object-oriented untuk API Apache yang
ditulis dalam C. Hasilnya, respon proses CGI lebih cepat, karena tidak
perlu lagi menjalankan interpreter Perl eksternal.

%description -l is.UTF-8
Mod_perl vinnur með perl á Apache vefþjóninum svo að Apache geti beint
keyrt Perl kóða. Mod_perl tengir Perl keyrslu söfnin við Apache
vefþjóninn og býður upp á hlutbundið Perl fyrir Apache C
forritunarmáls API. Það sem græðist er Hraðari CGI scriptur þar sem
það er engar úttengd Perl köll.

%description -l it.UTF-8
Mod_perl incorpora un interprete Perl nel server web Apache, in modo
che quest'ultimo possa eseguire direttamente il codice Perl. Mod_perl
collega la libreria runtime di Perl al server web Apache e fornisce
un'interfaccia Perl orientata all'oggetto per le API in linguaggio C
di Apache. In tal modo si velocizza il processo di turnaround degli
script CGI, poiché non è più necessario appoggiarsi ad un interprete
Perl esterno.

%description -l ja.UTF-8
mod_perl は、Apache Web サーバーが直接 Perl コードを実行できるように、
Perl インタープリタを Apache Web サーバーに組み込みます。mod_perl は、
Perl のランタイムライブラリを Apache Web サーバーにリンクさせ、Apache
の C 言語 API 用のオブジェクト指向の Perl インターフェイスを提供
します。その結果、外部の Perl インタープリタが起動する必要がないため、
CGI スクリプトのターンアラウンドプロセスが速くなります。

%description -l pl.UTF-8
Mod_perl jest modułem, który wyposaża serwer Apache w interpreter
Perla, umożliwiając w ten sposób bezpośrednie wykonywanie kodu Perla
przez serwer bez potrzeby angażowania zewnętrznego interpretera, co
przyspiesza procesy związane z uruchamianiem skryptów CGI.

%description -l pt.UTF-8
O mod_perl incorpora um interpretador de Perl no servidor Web Apache,
para que assim o servidor Web Apache possa executar directamente
código em Perl. O mod_perl associa a biblioteca de execução do Perl
com o servidor Web Apache e oferece uma interface orientada por
objectos do Perl para a API de C do Apache. O resultado final é um
processo de torneamento dos 'scripts' CGI mais rápido, dado que não
tem que se iniciar um interpretador de Perl externo.

%description -l ru.UTF-8
Mod_perl встраивает Perl-интрепретатор в WWW-сервер Apache, так что
этот сервер может напрямую работать с кодом Perl. Mod_perl связывает
библиотеку реального времени Perl с сервером Apache и содержит
объектно-ориентированный интерфейс Perl API языка Apache C. Конечный
результат - ускоренная работа со скриптами CGI.

%description -l sk.UTF-8
Mod_perl začleňuje interpreter Perlu do webového servera Apache;
server Apache potom môže priamo vykonávať príkazy Perlu. Mod_perl
zlinkuje knižnicu Perlu s webovým serverom Apache a poskytne tak
objektovo orietované rozhranie Perlu pre aplikačné rozhranie servera
Apache v jazyku C. Výsledkom je rýchlejšie vykonanie CGI skriptu, bez
akéhokoľvek spustenia externého interpretera jazyka Perl.

%description -l sv.UTF-8
Mod_perl införlivar en Perl-interpretator i webbservern Apache, så att
webbervern Apach kan köra Perl-kod direkt. Mod_perl länkar in Perls
körtidsbibliotek i webbservern Apache och ger ett objektorienterat
Perl-gränssnitt till Apaches API i språket C. Slutresultatet är en
snabbare processomsättning av CGI-skript, eftersom ingen extern
Perl-interpretator behöver startas.

%description -l uk.UTF-8
Проект інтеграції Apache та Perl дозволяє вам використовувати всю
потужність мови програмування Perl та web-серверу Apache. Це
досягається шляхом вбудовування бібліотек Perl всередину сервера
Apache через DSO та надання об'єктно-орієнтованих Perl-бібліотек для
доступу до Apache API.

Це досягається за допомогою mod_perl'а, котрий дозволяє створювати
модулі для Apache безпосередньо на мові Perl. Крім цього, це дозволяє
уникнути накладних витрат на завантаження інтерпретатора Perl при
обробці кожного запиту.

%description -l zh_CN.UTF-8
Mod_perl 将 Perl 解释程序与 Apache web 服务程序结合在一起，
以便后者可以直接执行 Perl 代码。 Mod_perl 将 Perl 运行时间程序库链接至
Apache web 服务程序， 并为 Apache 的 C 语言 API 提供面向对象的 Perl
接口。 由于不必启动任何外部 Perl 解释程序，因此会使 CGI
脚本回转过程更为快速。

%package devel
Summary:	Files needed for building XS modules that use mod_perl
Summary(pl.UTF-8):	Pliki potrzebne do budowania modułów XS korzystających z mod_perla
Group:		Development/Libraries
Requires:	apache-devel >= 2.0
Obsoletes:	mod_perl
Obsoletes:	mod_perl-common
Conflicts:	perl-modules < 1:5.8.6-6

%description devel
The apache-mod_perl-devel package contains the files needed for
building XS modules that use mod_perl.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki potrzebne do budowania modułów XS
korzystających z mod_perla.

%package -n perl-mod_%{mod_name}
Summary:	Perl APIs for mod_perl
Summary(pl.UTF-8):	Perlowe API dla mod_perla
Group:		Development/Languages/Perl

%description -n perl-mod_%{mod_name}
Perl APIs for mod_perl.

%description -n perl-mod_%{mod_name} -l pl.UTF-8
Perlowe API dla mod_perla.

%package -n perl-Apache-Test
Summary:	Apache::Test - Test.pm wrapper with helpers for testing Apache
Summary(pl.UTF-8):	Apache::Test - wrapper na Test.pm z funkcjami do testowania Apache
Version:	1.36
Group:		Development/Languages/Perl
Requires:	perl-mod_%{mod_name} = %{epoch}:%{ver}-%{release}
Requires:	perl-dirs >= 2.0-5

%description -n perl-Apache-Test
Apache::Test is a wrapper around the standard Test.pm with helpers for
testing an Apache server.

%description -n perl-Apache-Test -l pl.UTF-8
Apache::Test to moduł obudowujący standardowy Test.pm w funkcje
pomocnicze do testowania serwera Apache.

%prep
%setup -q -n mod_%{mod_name}-%{ver}-%{snap}
%patch0 -p1
%patch1 -p1

%build
%{__perl} Makefile.PL \
	MP_APXS=%{apxs} \
	MP_APR_CONFIG=%{_bindir}/apr-1-config \
	MP_APU_CONFIG=%{_bindir}/apu-1-config \
	INSTALLDIRS=vendor

%{__make} \
	OPTIMIZE="%{rpmcflags}" \
	MODPERL_OPTIMIZE="%{rpmcflags}" \
	CC="%{__cc}" \
	MP_APXS=%{apxs}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{apachelibdir},%{apacheconfdir}}

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name \*.orig -exec rm -f '{}' \;

install xs/tables/current/Apache2/* $RPM_BUILD_ROOT%{perl_vendorarch}/Apache2
install xs/tables/current/APR/* $RPM_BUILD_ROOT%{perl_vendorarch}/APR
install xs/tables/current/ModPerl/* $RPM_BUILD_ROOT%{perl_vendorarch}/ModPerl

install %{SOURCE1} $RPM_BUILD_ROOT%{apacheconfdir}/75_mod_perl.conf

# apache1-specific version - but mod_perl1 contains older Apache::SizeLimit which doesn't use shared Apache::SizeLimit::Core
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/Apache/SizeLimit.pm \
	$RPM_BUILD_ROOT%{_mandir}/man3/Apache::SizeLimit.3pm
# don't package Bundle::*
%{__rm} -r $RPM_BUILD_ROOT%{perl_vendorarch}/Bundle
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man3/Bundle*
# perl-specific cleanup
%{__rm} $RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/auto/mod_perl2/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%post
%service -q httpd restart

%postun
if [ "$1" = "0" ]; then
	%service -q httpd restart
fi

%files
%defattr(644,root,root,755)
%doc Changes INSTALL README STATUS
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{apacheconfdir}/75_mod_perl.conf
%attr(755,root,root) %{apachelibdir}/mod_perl.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/apache/mod_perl.h
%{_includedir}/apache/modperl_*.h

%files -n perl-mod_%{mod_name}
%defattr(644,root,root,755)
%{perl_vendorarch}/APR.pm
%{perl_vendorarch}/APR
%{perl_vendorarch}/Apache/Reload.pm
%{perl_vendorarch}/Apache/SizeLimit
%{perl_vendorarch}/Apache2
%{perl_vendorarch}/ModPerl
%{perl_vendorarch}/mod_perl2.pm
%dir %{perl_vendorarch}/auto/APR
%{perl_vendorarch}/auto/APR/APR.bs
%attr(755,root,root) %{perl_vendorarch}/auto/APR/APR.so
%dir %{perl_vendorarch}/auto/APR/[B-U]*
%{perl_vendorarch}/auto/APR/[B-U]*/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/APR/[B-U]*/*.so
%dir %{perl_vendorarch}/auto/Apache2
%dir %{perl_vendorarch}/auto/Apache2/[A-U]*
%{perl_vendorarch}/auto/Apache2/Build/autosplit.ix
%{perl_vendorarch}/auto/Apache2/[A-U]*/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Apache2/[A-U]*/*.so
%{perl_vendorarch}/auto/Apache2/typemap
%dir %{perl_vendorarch}/auto/ModPerl
%dir %{perl_vendorarch}/auto/ModPerl/[C-U]*
%{perl_vendorarch}/auto/ModPerl/[C-U]*/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/ModPerl/[C-U]*/*.so
%{_mandir}/man3/APR*.3pm*
%{_mandir}/man3/Apache::Reload.3pm*
%{_mandir}/man3/Apache::SizeLimit::Core.3pm*
%{_mandir}/man3/Apache2::*.3pm*
%{_mandir}/man3/ModPerl::*.3pm*
%{_mandir}/man3/mod_perl2.3pm*

%files -n perl-Apache-Test
%defattr(644,root,root,755)
%{perl_vendorarch}/Apache/Test*
%{_mandir}/man3/Apache::Test*.3pm*
