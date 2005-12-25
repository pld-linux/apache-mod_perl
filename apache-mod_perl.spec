# TODO:
# - separate perl-things from apache libs and configs (needed for some buildings)
# - separate devel things from runtime things (apache-mod_perl-2.0.2-2 marks perl-ExtUtils-MakeMaker-6.25_08-1 (cap perl(ExtUtils::Install)))
%include	/usr/lib/rpm/macros.perl
%define	apxs	/usr/sbin/apxs
Summary:	A Perl interpreter for the Apache Web server
Summary(cs):	Vestavìný interpret Perlu pro WWW server Apache
Summary(da):	En indbygget Perl-fortolker for webtjeneren Apache
Summary(de):	Ein eingebetteter Perl-Interpreter für den Apache Web-Server
Summary(es):	Intérprete Perl para el servidor Web Apache
Summary(fr):	Interpréteur Perl intégré pour le serveur Web Apache
Summary(id):	Interpreter Perl untuk web server Apache
Summary(is):	Perl túlkur fyrir Apache vefþjóninn
Summary(it):	Interprete Perl integrato per il server Web Apache
Summary(ja):	Apache Web ¥µ¡¼¥Ð¡¼ÍÑ¤ÎÁÈ¹þ¤ß Perl ¥¤¥ó¥¿¡¼¥×¥ê¥¿
Summary(nb):	En Perl-fortolker for webtjeneren Apache
Summary(pl):	Interpreter Perla dla serwera WWW Apache
Summary(pt):	Um interpretador de Perl embebido para o servidor Web Apache
Summary(ru):	÷ÓÔÒÏÅÎÎÙÊ ÉÎÔÅÒÐÒÅÔÁÔÏÒ Perl ÄÌÑ WWW-ÓÅÒ×ÅÒÁ Apache
Summary(sk):	Interpreter jazyka Perl pre webový server Apache
Summary(sl):	Vkljuèeni perlovski tolmaè za spletni stre¾nik Apache
Summary(sv):	En inbyggd Perl-interpretator för webbservern Apache
Summary(uk):	íÏÄÕÌØ ×ÂÕÄÏ×Õ×ÁÎÎÑ ¦ÎÔÅÒÐÒÅÔÁÔÏÒÁ Perl × ÓÅÒ×ÅÒ Apache
Summary(zh_CN):	ÓÃÓÚ Apache web ·þÎñ³ÌÐòµÄ Perl ½âÊÍ³ÌÐò¡£
Name:		apache-mod_perl
Version:	2.0.2
Release:	3
Epoch:		1
License:	Apache
Group:		Networking/Daemons
Source0:	http://perl.apache.org/dist/mod_perl-%{version}.tar.gz
# Source0-md5:	ad0a509fd34e3b8452887d80a1d45dea
Source1:	%{name}.conf
Patch0:		%{name}-Makefile_PL.patch
URL:		http://perl.apache.org/
BuildRequires:	apache-devel >= 2.0.55-1
BuildRequires:	apr-util-devel >= 1:1.0.0
BuildRequires:	expat-devel
BuildRequires:	gdbm-devel
BuildRequires:	openldap-devel
BuildRequires:	perl-devel >= 1:5.8.2
BuildRequires:	rpm-perlprov >= 3.0.3-16
%requires_eq_to	apache apache-devel
Provides:	apache(mod_perl)
Provides:	mod_perl
Requires:	apache(modules-api) = %apache_modules_api
Requires:	perl(DynaLoader) = %(%{__perl} -MDynaLoader -e 'print DynaLoader->VERSION')
# What's this mod_perl_hooks for?
Provides:	perl(mod_perl_hooks)
Provides:	perl-Apache-Test
Obsoletes:	mod_perl
Obsoletes:	mod_perl-common
Conflicts:	perl-modules < 1:5.8.6-6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# TODO: separate -devel with ExtUtils::Embed and friends?
%define		_noautoreq	'perl(Apache::.*)' 'perl(mod_perl)' 'perl(ModPerl::.*)' 'perl(ExtUtils::Embed)' 'perl(Module::Build)'
%define		_sysconfdir	%(%{apxs} -q SYSCONFDIR 2>/dev/null)
%define		_pkglibdir	%(%{apxs} -q LIBEXECDIR 2>/dev/null)

%description
Mod_perl incorporates a Perl interpreter into the Apache web server,
so that the Apache web server can directly execute Perl code. Mod_perl
links the Perl runtime library into the Apache web server and provides
an object-oriented Perl interface for Apache's C language API. The end
result is a quicker CGI script turnaround process, since no external
Perl interpreter has to be started.

%description -l cs
Modul mod_perl zaèleòuje interpret Perlu do WWW serveru Apache, tak¾e
WWW server mù¾e pøímo provádìt programy v Perlu. Mod_perl pøipojuje
bìhovou knihovnu Perlu do Apache WWW serveru a poskytuje objektovì
orientované perlovské rozhraní pro API serveru Apache. Výsledkem je
rychlej¹í start CGI skriptù, proto¾e nemusí být startován externí
interpret Perlu.

%description -l de
Mod_perl integriert einen Perl-Interpreter in den Apache Web-Server,
so dass dieser Perl-Code direkt ausführen kann. Das Programm verknüpft
die Perl-Runtime-Bibliothek mit dem Apache Web-Sever und stellt eine
objektorientierte Perl-Benutzeroberfläche für die C-API des
Apache-Servers bereit. Das Resultat ist eine schnellere Ausführung von
CGI-Skripten, da kein externer Perl-Interpreter gestartet werden muss.

%description -l es
Mod_perl incluye un intérprete Perl en el servidor Apache, de manera
que se puede ejecutar el código Perl directamente desde el servidor
Web. Mod_perl enumera las bibliotecas runtime del Perl al Web servidor
Apache y proporciona una interfaz Perl object-oriented para las API
del lenguaje C. De tal modo que se obtiene una ejecución más rápida de
los script CGI sin necesidad de apoyarse en un intérprete Perl.

%description -l fr
Mod_perl incorpore un interpréteur Perl dans le serveur Web Apache, de
manière à ce que le serveur Web Apache puisse exécuter directement du
code Perl. Mod_perl lie la bibliothèque d'exécution Perl au serveur
Web Apache et fournit une interface Perl orientée objet pour l'API en
langage C d'Apache. Le résultat final est une exécution des scripts
CGI plus rapide, du fait qu'aucun interpréteur Perl externe ne doit
être démarré.

%description -l id
Mod_perl memasukkan interpreter Perl ke dalam web server Apache,
sehingga Apache dapat secara langsung menjalankan kode Perl. Mod_perl
me-link runtime library Perl ke dalam web server Apache dan
menyediakan antarmuka Perl yang object-oriented untuk API Apache yang
ditulis dalam C. Hasilnya, respon proses CGI lebih cepat, karena tidak
perlu lagi menjalankan interpreter Perl eksternal.

%description -l is
Mod_perl vinnur með perl á Apache vefþjóninum svo að Apache geti beint
keyrt Perl kóða. Mod_perl tengir Perl keyrslu söfnin við Apache
vefþjóninn og býður upp á hlutbundið Perl fyrir Apache C
forritunarmáls API. Það sem græðist er Hraðari CGI scriptur þar sem
það er engar úttengd Perl köll.

%description -l it
Mod_perl incorpora un interprete Perl nel server web Apache, in modo
che quest'ultimo possa eseguire direttamente il codice Perl. Mod_perl
collega la libreria runtime di Perl al server web Apache e fornisce
un'interfaccia Perl orientata all'oggetto per le API in linguaggio C
di Apache. In tal modo si velocizza il processo di turnaround degli
script CGI, poiché non è più necessario appoggiarsi ad un interprete
Perl esterno.

%description -l ja
mod_perl ¤Ï¡¢Apache Web ¥µ¡¼¥Ð¡¼¤¬Ä¾ÀÜ Perl ¥³¡¼¥É¤ò¼Â¹Ô¤Ç¤­¤ë¤è¤¦¤Ë¡¢
Perl ¥¤¥ó¥¿¡¼¥×¥ê¥¿¤ò Apache Web ¥µ¡¼¥Ð¡¼¤ËÁÈ¤ß¹þ¤ß¤Þ¤¹¡£mod_perl ¤Ï¡¢
Perl ¤Î¥é¥ó¥¿¥¤¥à¥é¥¤¥Ö¥é¥ê¤ò Apache Web ¥µ¡¼¥Ð¡¼¤Ë¥ê¥ó¥¯¤µ¤»¡¢Apache
¤Î C ¸À¸ì API ÍÑ¤Î¥ª¥Ö¥¸¥§¥¯¥È»Ø¸þ¤Î Perl ¥¤¥ó¥¿¡¼¥Õ¥§¥¤¥¹¤òÄó¶¡
¤·¤Þ¤¹¡£¤½¤Î·ë²Ì¡¢³°Éô¤Î Perl ¥¤¥ó¥¿¡¼¥×¥ê¥¿¤¬µ¯Æ°¤¹¤ëÉ¬Í×¤¬¤Ê¤¤¤¿¤á¡¢
CGI ¥¹¥¯¥ê¥×¥È¤Î¥¿¡¼¥ó¥¢¥é¥¦¥ó¥É¥×¥í¥»¥¹¤¬Â®¤¯¤Ê¤ê¤Þ¤¹¡£

%description -l pl
Mod_perl jest modu³em, który wyposa¿a serwer Apache w interpreter
Perla, umo¿liwiaj±c w ten sposób bezpo¶rednie wykonywanie kodu Perla
przez serwer bez potrzeby anga¿owania zewnêtrznego interpretera, co
przyspiesza procesy zwi±zane z uruchamianiem skryptów CGI.

%description -l pt
O mod_perl incorpora um interpretador de Perl no servidor Web Apache,
para que assim o servidor Web Apache possa executar directamente
código em Perl. O mod_perl associa a biblioteca de execução do Perl
com o servidor Web Apache e oferece uma interface orientada por
objectos do Perl para a API de C do Apache. O resultado final é um
processo de torneamento dos 'scripts' CGI mais rápido, dado que não
tem que se iniciar um interpretador de Perl externo.

%description -l ru
Mod_perl ×ÓÔÒÁÉ×ÁÅÔ Perl-ÉÎÔÒÅÐÒÅÔÁÔÏÒ × WWW-ÓÅÒ×ÅÒ Apache, ÔÁË ÞÔÏ
ÜÔÏÔ ÓÅÒ×ÅÒ ÍÏÖÅÔ ÎÁÐÒÑÍÕÀ ÒÁÂÏÔÁÔØ Ó ËÏÄÏÍ Perl. Mod_perl Ó×ÑÚÙ×ÁÅÔ
ÂÉÂÌÉÏÔÅËÕ ÒÅÁÌØÎÏÇÏ ×ÒÅÍÅÎÉ Perl Ó ÓÅÒ×ÅÒÏÍ Apache É ÓÏÄÅÒÖÉÔ
ÏÂßÅËÔÎÏ-ÏÒÉÅÎÔÉÒÏ×ÁÎÎÙÊ ÉÎÔÅÒÆÅÊÓ Perl API ÑÚÙËÁ Apache C. ëÏÎÅÞÎÙÊ
ÒÅÚÕÌØÔÁÔ - ÕÓËÏÒÅÎÎÁÑ ÒÁÂÏÔÁ ÓÏ ÓËÒÉÐÔÁÍÉ CGI.

%description -l sk
Mod_perl zaèleòuje interpreter Perlu do webového servera Apache;
server Apache potom mô¾e priamo vykonáva» príkazy Perlu. Mod_perl
zlinkuje kni¾nicu Perlu s webovým serverom Apache a poskytne tak
objektovo orietované rozhranie Perlu pre aplikaèné rozhranie servera
Apache v jazyku C. Výsledkom je rýchlej¹ie vykonanie CGI skriptu, bez
akéhokoµvek spustenia externého interpretera jazyka Perl.

%description -l sv
Mod_perl införlivar en Perl-interpretator i webbservern Apache, så att
webbervern Apach kan köra Perl-kod direkt. Mod_perl länkar in Perls
körtidsbibliotek i webbservern Apache och ger ett objektorienterat
Perl-gränssnitt till Apaches API i språket C. Slutresultatet är en
snabbare processomsättning av CGI-skript, eftersom ingen extern
Perl-interpretator behöver startas.

%description -l uk
ðÒÏÅËÔ ¦ÎÔÅÇÒÁÃ¦§ Apache ÔÁ Perl ÄÏÚ×ÏÌÑ¤ ×ÁÍ ×ÉËÏÒÉÓÔÏ×Õ×ÁÔÉ ×ÓÀ
ÐÏÔÕÖÎ¦ÓÔØ ÍÏ×É ÐÒÏÇÒÁÍÕ×ÁÎÎÑ Perl ÔÁ web-ÓÅÒ×ÅÒÕ Apache. ãÅ
ÄÏÓÑÇÁ¤ÔØÓÑ ÛÌÑÈÏÍ ×ÂÕÄÏ×Õ×ÁÎÎÑ Â¦ÂÌ¦ÏÔÅË Perl ×ÓÅÒÅÄÉÎÕ ÓÅÒ×ÅÒÁ
Apache ÞÅÒÅÚ DSO ÔÁ ÎÁÄÁÎÎÑ ÏÂ'¤ËÔÎÏ-ÏÒ¦¤ÎÔÏ×ÁÎÉÈ Perl-Â¦ÂÌ¦ÏÔÅË ÄÌÑ
ÄÏÓÔÕÐÕ ÄÏ Apache API.

ãÅ ÄÏÓÑÇÁ¤ÔØÓÑ ÚÁ ÄÏÐÏÍÏÇÏÀ mod_perl'Á, ËÏÔÒÉÊ ÄÏÚ×ÏÌÑ¤ ÓÔ×ÏÒÀ×ÁÔÉ
ÍÏÄÕÌ¦ ÄÌÑ Apache ÂÅÚÐÏÓÅÒÅÄÎØÏ ÎÁ ÍÏ×¦ Perl. ëÒ¦Í ÃØÏÇÏ, ÃÅ ÄÏÚ×ÏÌÑ¤
ÕÎÉËÎÕÔÉ ÎÁËÌÁÄÎÉÈ ×ÉÔÒÁÔ ÎÁ ÚÁ×ÁÎÔÁÖÅÎÎÑ ¦ÎÔÅÒÐÒÅÔÁÔÏÒÁ Perl ÐÒÉ
ÏÂÒÏÂÃ¦ ËÏÖÎÏÇÏ ÚÁÐÉÔÕ.

%description -l zh_CN
Mod_perl ½« Perl ½âÊÍ³ÌÐòÓë Apache web ·þÎñ³ÌÐò½áºÏÔÚÒ»Æð£¬
ÒÔ±ãºóÕß¿ÉÒÔÖ±½ÓÖ´ÐÐ Perl ´úÂë¡£ Mod_perl ½« Perl ÔËÐÐÊ±¼ä³ÌÐò¿âÁ´½ÓÖÁ
Apache web ·þÎñ³ÌÐò£¬ ²¢Îª Apache µÄ C ÓïÑÔ API Ìá¹©ÃæÏò¶ÔÏóµÄ Perl
½Ó¿Ú¡£ ÓÉÓÚ²»±ØÆô¶¯ÈÎºÎÍâ²¿ Perl ½âÊÍ³ÌÐò£¬Òò´Ë»áÊ¹ CGI
½Å±¾»Ø×ª¹ý³Ì¸üÎª¿ìËÙ¡£

%prep
%setup -q -n mod_perl-%{version}
%patch0 -p1

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

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pkglibdir},%{_sysconfdir}/httpd.conf}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name \*.orig -exec rm -f '{}' \;

install xs/tables/current/Apache2/* $RPM_BUILD_ROOT%{perl_vendorarch}/Apache2
install xs/tables/current/APR/* $RPM_BUILD_ROOT%{perl_vendorarch}/APR
install xs/tables/current/ModPerl/* $RPM_BUILD_ROOT%{perl_vendorarch}/ModPerl

rm -rf $RPM_BUILD_ROOT%{perl_vendorarch}/Bundle
rm -f $RPM_BUILD_ROOT%{_mandir}/man?/Bundle*
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/httpd.conf/75_mod_perl.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache HTTP daemon."
fi

%preun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%files
%defattr(644,root,root,755)
%doc Changes INSTALL README STATUS
%attr(755,root,root) %{_pkglibdir}/*.so
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*.conf

%{perl_vendorarch}/*.pm
%{perl_vendorarch}/APR
%{perl_vendorarch}/Apache
%{perl_vendorarch}/Apache2
%{perl_vendorarch}/ModPerl

%dir %{perl_vendorarch}/auto/*
%{perl_vendorarch}/auto/*/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/*/*.so
%dir %{perl_vendorarch}/auto/APR/[B-U]*
%dir %{perl_vendorarch}/auto/Apache2/[A-U]*
%dir %{perl_vendorarch}/auto/ModPerl/*
%{perl_vendorarch}/auto/*/*/*.ix
%{perl_vendorarch}/auto/*/*/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/*/*/*.so

%{perl_vendorarch}/auto/Apache2/typemap
# to -devel? directory ownership problem...
%{_includedir}/apache/*.h

%{_mandir}/man?/*
