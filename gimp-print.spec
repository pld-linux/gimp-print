Summary:	Collection of high-quality printer drivers
Summary(pl):	Zestaw wysokiej jako¶ci sterowników do drukarek
Summary(pt_BR):	plugin GIMP-Print para impressão de imagens em alta qualidade
Name:		gimp-print
Version:	4.2.0
Release:	1
License:	GPL
Group:		Applications/Printing
Group(cs):	Aplikace/Tisk
Group(da):	Programmer/Udskrift
Group(de):	Applikationen/Drucken
Group(es):	Aplicaciones/Impresión
Group(fr):	Applications/Impression
Group(it):	Applicazioni/Stampa
Group(no):	Applikasjoner/Utskrift
Group(pl):	Aplikacje/Drukowanie
Group(pt):	Aplicações/Impressão
Group(ru):	ðÒÉÌÏÖÅÎÉÑ/ðÅÞÁÔØ
Group(sv):	Tillämpningar/Utskrift
Source0:	http://prdownloads.sourceforge.net/gimp-print/%{name}-%{version}.tar.gz
Patch0:		%{name}-install.patch
Patch1:		%{name}-info.patch
Patch2:		%{name}-usb.patch
URL:		http://gimp-print.sf.net/
BuildRequires:	gimp-devel >= 1:1.2.2-5
BuildRequires:	cups-devel >= 1.1.9
BuildRequires:	/usr/bin/texi2html
BuildRequires:	tetex-dvips
BuildRequires:	texinfo
BuildRequires:	/usr/bin/db2html
BuildRequires:	/usr/bin/db2ps
BuildRequires:	/usr/bin/db2pdf
Requires:	gimp >= 1:1.2.2-5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gimp-Print is a collection of very high quality printer drivers for
UNIX/Linux. The goal of this project is uncompromising print quality
and robustness. Included with this package is the Print plugin for the
GIMP (hence the name), a CUPS driver, and a driver for Ghostscript
that may be compiled into that package. This driver package is
Foomatic-compatible to enable plug and play with many print spoolers.
In addition, various printer maintenance utilities are included. Many
users report that the quality of Gimp-Print on high end Epson Stylus
printers matches or exceeds the quality of the drivers supplied for
Windows and Macintosh.

%description -l pl
Gimp-Print to zbiór bardzo wysokiej jako¶ci sterowników do drukarek
dla systemów UNIX/Linux. Celem tego projektu jest jak najlepsza jako¶æ
wydruku. Do³±czone do tego pakietu s±: wtyczka dla programu GIMP (st±d
nazwa), sterownik CUPS i sterownik Ghostscriptu. Sterownik umo¿liwia
bezpo¶redni± wspó³pracê z wieloma kolejkami wydruku. Dodatkowo
do³±czonych jest wiele programów do obs³ugi drukarki. Wielu
u¿ytkowników twierdzi ze jako¶æ wydruków na najlepszych drukarkach
Epson Stylus dorównuje albo nawet przerasta jako¶ci± to, co jest
oferowane przez sterowniki dla Windows i MacOS.

%description -l pt_BR
Este é um plugin para o Gimp que permite a impressão de imagens e
fotos em uma qualidade muito boa em várias impressoras de jato de
tinta modernas e em algumas lasers. Especialmente nas impressoras
Epsion Stylus a qualidade se equipara a mesma obtida em sistema
operacionais proprietários, uma vez que a Epson publicou as
especificações dos protocolos usados por suas impressoras. Outras
marcas de impressoras como HP também atingem qualidades altas de
impressão. Esse plugin também é capaz de gerar arquivos Postscript que
permite ser usado em qualquer outra impressora.

%package lib
Summary:	gimp-print library
Summary(pl):	Biblioteka Gimp-print
Summary(pt_BR):	Bibliotecas dinâmicas para impressão de alta qualidade
Group:		Libraries
Group(cs):	Knihovny
Group(da):	Biblioteker
Group(de):	Bibliotheken
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(it):	Librerie
Group(ja):	¥é¥¤¥Ö¥é¥ê
Group(no):	Biblioteker
Group(pl):	Biblioteki
Group(pt):	Bibliotecas
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(sv):	Bibliotek
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ

%description lib
Gimp-print library.

%description lib -l pl
Biblioteka Gimp-print.

%description lib -l pt_BR
Esse pacote contém bibliotecas dinâmicas de alta qualidade para serem
usados pelo plugin do Gimp gimp-print, pelo driver "stp" do
ghostscript e por drivers especializados do CUPS

%package devel
Summary:	gimp-print development tools
Summary(pl):	Pliki nag³ówkowe itp. do gimp-print
Summary(pt_BR):	Cabeçalhos e arquivos de desenvolvimento para o libgimpprint
Group:		Development/Libraries
Group(cs):	Vývojové prostøedky/Knihovny
Group(da):	Udvikling/Biblioteker
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(it):	Sviluppo/Librerie
Group(ja):	³«È¯/¥é¥¤¥Ö¥é¥ê
Group(no):	Utvikling/Bibliotek
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(pt):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(sv):	Utveckling/Bibliotek
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name}-lib = %{version}-%{release}

%description devel
Gimp-print development tools and headers.

%description devel -l pl
Nag³ówki i narzêdzia deweloperskie dla Gimp-print.

%description devel -l pt_BR
Este são os arquivos de desenvolvimento para compilar programas com a
biblioteca libgimpprint.

%package static
Summary:	gimp-print static libraries
Summary(pl):	Statyczne biblioteki gimp-print
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento com gimp-print
Group:		Development/Libraries
Group(cs):	Vývojové prostøedky/Knihovny
Group(da):	Udvikling/Biblioteker
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(it):	Sviluppo/Librerie
Group(ja):	³«È¯/¥é¥¤¥Ö¥é¥ê
Group(no):	Utvikling/Bibliotek
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(pt):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(sv):	Utveckling/Bibliotek
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name}-devel = %{version}-%{release}

%description static
Gimp-print static libraries.

%description static -l pl
Biblioteki statyczne Gimp-print.

%description static -l pt_BR
Bibliotecas estáticas para desenvolvimento com gimp-print.

%package -n escputil
Summary:	Tool for Epson ink printers
Summary(pl):	Narzêdzie do drukarek atramentowych Epson
Summary(pt_BR):	Ferramenta de manutenção de impressoras ESPSON Stylus (R)
Group:		Applications/Printing
Group(cs):	Aplikace/Tisk
Group(da):	Programmer/Udskrift
Group(de):	Applikationen/Drucken
Group(es):	Aplicaciones/Impresión
Group(fr):	Applications/Impression
Group(it):	Applicazioni/Stampa
Group(no):	Applikasjoner/Utskrift
Group(pl):	Aplikacje/Drukowanie
Group(pt):	Aplicações/Impressão
Group(ru):	ðÒÉÌÏÖÅÎÉÑ/ðÅÞÁÔØ
Group(sv):	Tillämpningar/Utskrift

%description -n escputil
ESPSON Stylus (R) Printers Maintenance tool. This command line tool
can be used to perform the following tests:
- Clean head
- Nozzle check
- Align Head
- Printer Status
- Ink level
- Printer Identidy

%description -n escputil -l pl
Narzêdzie dla drukarek atramentowych Epson.

%description -n escputil -l pt_BR
Ferramenta de manutenção de impressoras ESPSON Stylus (R). Esta
ferramenta de linha de comando é usada para executar as seguintes
tarefas:
- Limpeza de cabeçote
- Checagem de Qualidade de impressão
- Alinhamento de cabeçote
- Estado da Impressora
- Nível de tinta
- Identificação da Impressora

%package cups
Summary:	gimp-print as CUPS plugin
Summary(pl):	gimp-print jako wtyczka do CUPS
Summary(pt_BR):	Entradas ppd para serem usadas com o cups
Group:		Applications/Printing
Group(cs):	Aplikace/Tisk
Group(da):	Programmer/Udskrift
Group(de):	Applikationen/Drucken
Group(es):	Aplicaciones/Impresión
Group(fr):	Applications/Impression
Group(it):	Applicazioni/Stampa
Group(no):	Applikasjoner/Utskrift
Group(pl):	Aplikacje/Drukowanie
Group(pt):	Aplicações/Impressão
Group(ru):	ðÒÉÌÏÖÅÎÉÑ/ðÅÞÁÔØ
Group(sv):	Tillämpningar/Utskrift
Requires:	cups >= 1.1.9

%description cups
Gimp-print as CUPS plugin.

%description cups -l pl
Plugin gimp-print dla CUPS.

%description cups -l pt_BR
Este pacote contém os arquivos ppd para se usar o driver Gimp-Print
com o sistema de impressão cups.

%package samples
Summary:	gimp-print samples
Summary(pl):	Przyk³ady do gimp-print
Group:		Applications/Printing
Group(cs):	Aplikace/Tisk
Group(da):	Programmer/Udskrift
Group(de):	Applikationen/Drucken
Group(es):	Aplicaciones/Impresión
Group(fr):	Applications/Impression
Group(it):	Applicazioni/Stampa
Group(no):	Applikasjoner/Utskrift
Group(pl):	Aplikacje/Drukowanie
Group(pt):	Aplicações/Impressão
Group(ru):	ðÒÉÌÏÖÅÎÉÑ/ðÅÞÁÔØ
Group(sv):	Tillämpningar/Utskrift

%description samples
Gimp-print samples.

%description samples -l pl
Przyk³ady dla Gimp-print.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%configure2_13 \
	--with-cups \
	--with-gimp \
	--enable-escputil \
	--enable-libgimpprint \
	--with-samples \
	--with-user-guide \
	--without-ghost 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_datadir}/gimp-print/doc doc-installed
mv -f doc-installed/manual-html doc-installed/manual
mv -f doc-installed/html doc-instlled/user-guide
mv -f $RPM_BUILD_ROOT%{_datadir}/gimp-print/samples \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}

gzip -9nf README ChangeLog AUTHORS README NEWS \
	src/cups/README src/cups/commands.txt

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	lib -p /sbin/ldconfig
%postun	lib -p /sbin/ldconfig

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files 
%defattr(644,root,root,755)
%attr(755,root,root) %(gimptool --gimpplugindir)/plug-ins/*

%files lib -f %{name}.lang
%defattr(644,root,root,755)
%doc doc-installed/user-guide doc-installed/manual doc/FAQ.html AUTHORS.gz README.gz NEWS.gz ChangeLog.gz
%attr(755,root,root) %{_libdir}/libgimpprint.so.1.0.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgimpprint.so
%attr(755,root,root) %{_libdir}/libgimpprint.la
%attr(755,root,root) %{_bindir}/gimpprint-config
%{_includedir}/gimp-print
%{_aclocaldir}/gimpprint.m4
%{_mandir}/man1/gimpprint-config.1*
%{_mandir}/man3/gimpprint.3*
%{_datadir}/info/*info*

%files static
%defattr(644,root,root,755)
%{_libdir}/libgimpprint.a

%files -n escputil
%defattr(644,root,root,755)
%{_mandir}/man1/escputil.1*
%attr(755,root,root) %{_bindir}/escputil

%files cups
%defattr(644,root,root,755)
%doc src/cups/README.gz src/cups/commands.txt.gz src/cups/commands
%{_sysconfdir}/cups/command.types
%attr(755,root,root) %{_bindir}/cups-calibrate
%{_datadir}/cups/calibrate.ppm
%{_datadir}/cups/model/C/*
%lang(da) %{_datadir}/cups/model/da/*
%lang(en_GB) %{_datadir}/cups/model/en_GB/*
%lang(fr) %{_datadir}/cups/model/fr/*
%lang(no) %{_datadir}/cups/model/no/*
%lang(pl) %{_datadir}/cups/model/pl/*
%lang(sv) %{_datadir}/cups/model/sv/*
%attr(755,root,root) %{_libdir}/cups/backend/*
%attr(755,root,root) %{_libdir}/cups/filter/*
%{_mandir}/man8/cups-calibrate.8*

%files samples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}
