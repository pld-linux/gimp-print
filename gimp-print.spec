#
# Conditional build:
# _without_cups		- without CUPS subpackage
# _without_gimp		- without GIMP plugin subpackage
# _without_ijs		- without IJS server for Ghostscript
# _without_foomatic	- don't generate foomatic data
# _with_static          - enable building static library
#
# TODO:
# - port info_and_pdf_only.patch and install documentation in correct place.
# - think about not including PPDs in package and allow generation by cups-genppd
#
%include	/usr/lib/rpm/macros.perl
Summary:	Collection of high-quality printer drivers
Summary(pl):	Zestaw wysokiej jako¶ci sterowników do drukarek
Summary(pt_BR):	plugin GIMP-Print para impressão de imagens em alta qualidade
Name:		gimp-print
Version:	4.3.8
Release:	0.2
License:	GPL
Group:		Applications/Printing
Source0:	http://prdownloads.sourceforge.net/gimp-print/%{name}-%{version}.tar.bz2
Patch0:		%{name}-info.patch
Patch1:		%{name}-usb.patch
Patch2:		%{name}-gettext.patch
Patch3:		%{name}-info_and_pdf_only.patch
URL:		http://gimp-print.sf.net/
%{!?_without_cups:BuildRequires:	cups-devel >= 1.1.9}
BuildRequires:	docbook-style-dsssl
BuildRequires:	docbook-utils
%{!?_without_foomatic:BuildRequires:	foomatic-db-engine >= 2.9.1}
BuildRequires:	gettext-autopoint
%{!?_without_ijs:BuildRequires:	ghostscript-ijs-devel}
%{!?_without_gimp:BuildRequires:	gimp-devel >= 1:1.2.3-1.4}
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	texinfo
BuildRequires:	texinfo-texi2dvi
Requires:	gimp >= 1:1.2.2-5
Requires:	libgimpprint = %{version}
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

%package -n libgimpprint
Summary:	gimp-print library
Summary(pl):	Biblioteka gimp-print
Summary(pt_BR):	Bibliotecas dinâmicas para impressão de alta qualidade
Group:		Libraries
Obsoletes:	gimp-print-lib 

%description -n libgimpprint
Gimp-print library.

%description -n libgimpprint -l pl
Biblioteka Gimp-print.

%description -n libgimpprint -l pt_BR
Esse pacote contém bibliotecas dinâmicas de alta qualidade para serem
usados pelo plugin do Gimp gimp-print, pelo driver "stp" do
ghostscript e por drivers especializados do CUPS

%package -n libgimpprint-devel
Summary:	gimp-print development tools
Summary(pl):	Pliki nag³ówkowe itp. do gimp-print
Summary(pt_BR):	Cabeçalhos e arquivos de desenvolvimento para o libgimpprint
Group:		Development/Libraries
Requires:	libgimpprint = %{version}-%{release}
Obsoletes:	gimp-print-devel

%description -n libgimpprint-devel
Gimp-print development tools and headers.

%description -n libgimpprint-devel -l pl
Nag³ówki i narzêdzia deweloperskie dla Gimp-print.

%description -n libgimpprint-devel -l pt_BR
Este são os arquivos de desenvolvimento para compilar programas com a
biblioteca libgimpprint.

%package -n libgimpprint-static
Summary:	gimp-print static libraries
Summary(pl):	Statyczne biblioteki gimp-print
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento com gimp-print
Group:		Development/Libraries
Requires:	libgimpprint-devel = %{version}-%{release}
Obsoletes:	gimp-print-static

%description -n libgimpprint-static
Gimp-print static libraries.

%description -n libgimpprint-static -l pl
Biblioteki statyczne Gimp-print.

%description -n libgimpprint-static -l pt_BR
Bibliotecas estáticas para desenvolvimento com gimp-print.

%package -n libgimpprintui
Summary:	gimp-print UI library
Summary(pl):	Biblioteka gimp-print
Summary(pt_BR):	Bibliotecas dinâmicas para impressão de alta qualidade
Group:		Libraries
Obsoletes:	gimp-print-lib 
Requires:	libgimpprint = %{version}-%{release}

%description -n libgimpprintui
Gimp-print library.

%description -n libgimpprintui -l pl
Biblioteka Gimp-print.

%description -n libgimpprintui -l pt_BR
Esse pacote contém bibliotecas dinâmicas de alta qualidade para serem
usados pelo plugin do Gimp gimp-print, pelo driver "stp" do
ghostscript e por drivers especializados do CUPS

%package -n libgimpprintui-devel
Summary:	gimp-print development tools
Summary(pl):	Pliki nag³ówkowe itp. do gimp-print
Summary(pt_BR):	Cabeçalhos e arquivos de desenvolvimento para o libgimpprint
Group:		Development/Libraries
Requires:	libgimpprintui = %{version}-%{release}
Obsoletes:	gimp-print-devel

%description -n libgimpprintui-devel
Gimp-print development tools and headers.

%description -n libgimpprintui-devel -l pl
Nag³ówki i narzêdzia deweloperskie dla Gimp-print.

%description -n libgimpprintui-devel -l pt_BR
Este são os arquivos de desenvolvimento para compilar programas com a
biblioteca libgimpprint.

%package -n libgimpprintui-static
Summary:	gimp-print static libraries
Summary(pl):	Statyczne biblioteki gimp-print
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento com gimp-print
Group:		Development/Libraries
Requires:	libgimpprintui-devel = %{version}-%{release}
Obsoletes:	gimp-print-static

%description -n libgimpprintui-static
Gimp-print static libraries.

%description -n libgimpprintui-static -l pl
Biblioteki statyczne Gimp-print.

%description -n libgimpprintui-static -l pt_BR
Bibliotecas estáticas para desenvolvimento com gimp-print.


%package -n escputil
Summary:	Tool for Epson ink printers
Summary(pl):	Narzêdzie do drukarek atramentowych Epson
Summary(pt_BR):	Ferramenta de manutenção de impressoras ESPSON Stylus (R)
Group:		Applications/Printing

%description -n escputil
ESPSON Stylus (R) Printers Maintenance tool. This command line tool
can be used to perform the following tests:
- Clean head
- Nozzle check
- Align Head
- Printer Status
- Ink level
- Printer Identify

%description -n escputil -l pl
Dzia³aj±ce z linii poleceñ narzêdzie dla drukarek atramentowych Epson.
Mo¿e byæ u¿yte do:
- oczyszczenia g³owicy
- testu dysz
- wyrównania g³owicy
- odczytu stanu drukarki
- odczytu ilo¶ci tuszu
- identyfikacji drukarki.

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
Requires:	cups >= 1.1.9

%description cups
Gimp-print as CUPS plugin.

%description cups -l pl
Wtyczka gimp-print dla CUPS.

%description cups -l pt_BR
Este pacote contém os arquivos ppd para se usar o driver Gimp-Print
com o sistema de impressão cups.

%package samples
Summary:	gimp-print samples
Summary(pl):	Przyk³ady do gimp-print
Group:		Applications/Printing

%description samples
Gimp-print samples.

%description samples -l pl
Przyk³ady dla Gimp-print.

%package ijs
Summary:	gimp-print IJS driver for GhostScript
Summary(pl):	Sterownik IJS Gimp-print dla GhostScript
Group:		Applications/Printing
Requires:	libgimpprint = %{version}-%{release}

%description ijs
Gimp-print IJS driver for GhostScript.

%description ijs -l pl
Sterownik IJS Gimp-print dla GhostScript.

%package -n foomatic-db-gimp-print
Summary:	foomatic data for gimp-print IJS driver
Summary(pl):	Dane foomatic dla sterownika IJS gimp-print
Group:		Applications/Printing
Requires:	%{name}-ijs = %{version}-%{release}
Requires:	foomatic-db-engine >= 2.9.1

%description -n foomatic-db-gimp-print
foomatic data for gimp-print IJS driver.

%description -n foomatic-db-gimp-print -l pl
Dane foomatic dla sterownika IJS gimp-print.

%prep 
%setup  -q 
%patch0 -p1
%patch1 -p1
%patch2 -p1 
#%patch3 -p1

# hack for gimp 1.3, but not sufficient to build
#if [ -f %{_aclocaldir}/gimp-1.4.m4 ]; then
#	echo 'AC_DEFUN([AM_PATH_GIMP],AM_PATH_GIMP_1_4)' > m4/gimp14.m4
#fi

%build
rm -f m4extra/{libtool.m4,gettext.m4,lcmessage.m4,progtest.m4}
%{!?_without_gimp:rm -f m4extra/gimp.m4}
%{__libtoolize}
%{__autopoint}
aclocal -I m4 -I m4extra
touch src/main/gimpprint.pc.in \
	src/libgimpprintui/gimpprint-ui.pc.in
%{__automake}
%{__autoconf}

%configure \
	%{?debug:--enable-debug} \
	--with%{?_without_cups:out}-cups \
	--with%{?_without_gimp:out}-gimp \
	--with%{?_without_ijs:out}-ijs \
	--with%{?_without_foomatic:out}-foomatic \
	%{?_with_static:--enable-static} \
	--with-modules=dlopen \
	--enable-escputil \
	--enable-libgimpprint \
	%{?_without_cups:--disable-cups-ppds} \
	--disable-translated-cups-ppds \
	--enable-cups-level3-ppds \
	--enable-lexmarkutil \
	--enable-samples \
	--enable-user-guide \
	--enable-xmldef \
	--disable-rpath \
	--without-ghost 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_datadir}/gimp-print/doc doc-installed
#mv -f doc-installed/manual-html doc-installed/manual
#mv -f doc-installed/html doc-installed/user-guide
mv -f $RPM_BUILD_ROOT%{_datadir}/gimp-print/samples \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}
rm -f $RPM_BUILD_ROOT%{_mandir}/man8/update-cups-genppd.8
echo '.so cups-genppdconfig.8' > $RPM_BUILD_ROOT%{_mandir}/man8/update-cups-genppd.8

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n libgimpprint -p /sbin/ldconfig
%postun	-n libgimpprint -p /sbin/ldconfig
%post	-n libgimpprintui -p /sbin/ldconfig
%postun	-n libgimpprintui -p /sbin/ldconfig

%post -n libgimpprint-devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun -n libgimpprint-devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%if %{?!_without_gimp:1}0
%files
%defattr(644,root,root,755)
%attr(755,root,root) %(gimptool --gimpplugindir)/plug-ins/*
%endif

%files -n libgimpprint -f %{name}.lang
%defattr(644,root,root,755)
%doc doc-installed/gimpprint.ps doc-installed/html doc-installed/users-guide.pdf
%doc doc/FAQ.html AUTHORS README NEWS ChangeLog
%attr(755,root,root) %{_libdir}/libgimpprint-*.so
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/%{version}
%dir %{_libdir}/%{name}/%{version}/modules
%attr(755,root,root) %{_libdir}/%{name}/%{version}/modules/*.so
%{_datadir}/%{name}/%{version}
%{_mandir}/man7/*

%files -n libgimpprintui
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgimpprintui-*.so

%files -n libgimpprint-devel
%defattr(644,root,root,755)
%doc doc-installed/developer-html
%attr(755,root,root) %{_libdir}/libgimpprint.so
%{_libdir}/libgimpprint.la
%{_pkgconfigdir}/gimpprint.pc
%{_includedir}/gimp-print
%{_mandir}/man1/gimpprint-config.1*
%{_mandir}/man3/gimpprint.3*
%{_datadir}/info/*info*

%files -n libgimpprintui-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgimpprintui.so
%{_libdir}/libgimpprintui.la
%{_pkgconfigdir}/gimpprint-ui.pc
%{_includedir}/gimp-print

%if %{?_with_static:1}0
%files -n libgimpprint-static
%defattr(644,root,root,755)
%{_libdir}/libgimpprint.a

%files -n libgimpprintui-static
%defattr(644,root,root,755)
%{_libdir}/libgimpprintui.a
%endif

%files -n escputil
%defattr(644,root,root,755)
%{_mandir}/man1/escputil.1*
%attr(755,root,root) %{_bindir}/escputil

%if %{!?_without_cups:1}0
%files cups
%defattr(644,root,root,755)
%doc src/cups/README src/cups/command.txt src/cups/commands
%{_sysconfdir}/cups/command.types
%attr(755,root,root) %{_bindir}/cups-*
%attr(755,root,root) %{_sbindir}/cups-*
%{_datadir}/cups/calibrate.ppm
#%{_datadir}/cups/model/C/*
%{_datadir}/cups/model/gimp-print/en/*
#%lang(en_GB) %{_datadir}/cups/model/gimp-print/en_GB/*
#%lang(da) %{_datadir}/cups/model/gimp-print/da/*
#%lang(de) %{_datadir}/cups/model/gimp-print/de/*
#%lang(el) %{_datadir}/cups/model/gimp-print/el/*
#%lang(es) %{_datadir}/cups/model/gimp-print/es/*
#%lang(fr) %{_datadir}/cups/model/gimp-print/fr/*
#%lang(nl) %{_datadir}/cups/model/gimp-print/nl/*
#%lang(no) %{_datadir}/cups/model/gimp-print/no/*
#%lang(pl) %{_datadir}/cups/model/gimp-print/pl/*
#%lang(pt) %{_datadir}/cups/model/gimp-print/pt/*
#%lang(sk) %{_datadir}/cups/model/gimp-print/sk/*
#%lang(sv) %{_datadir}/cups/model/gimp-print/sv/*
%attr(755,root,root) %{_libdir}/cups/backend/*
%attr(755,root,root) %{_libdir}/cups/filter/*
%{_mandir}/man8/*cups*.8*
%endif

%files samples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}

%if %{!?_without_ijs:1}0
%files ijs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ijsgimpprint
%{_mandir}/man1/ijsgimpprint.1*
%endif

%if %{!?_without_foomatic:1}0
%files -n foomatic-db-gimp-print
%defattr(644,root,root,755)
%{_datadir}/foomatic/db/source/driver/*
%{_datadir}/foomatic/db/source/opt/*
%endif
