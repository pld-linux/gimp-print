#
# Conditional build:
%bcond_without	cups	# don't build CUPS plugin
%bcond_with	gimp	# build GIMP 1.2.x plugin subpackage
%bcond_without	ijs	# don't build IJS server for Ghostscript
#
Summary:	Collection of high-quality printer drivers
Summary(pl.UTF-8):   Zestaw wysokiej jakości sterowników do drukarek
Summary(pt_BR.UTF-8):   plugin GIMP-Print para impressão de imagens em alta qualidade
Name:		gimp-print
Version:	4.2.7
Release:	1
License:	GPL
Group:		Applications/Printing
Source0:	http://dl.sourceforge.net/gimp-print/%{name}-%{version}.tar.gz
# Source0-md5:	766be49f44a6a682d857e5aefec414d4
Patch0:		%{name}-info.patch
Patch1:		%{name}-usb.patch
Patch2:		%{name}-info_and_pdf_only.patch
Patch3:		%{name}-opt.patch
Patch4:		%{name}-nolibs.patch
Patch5:		%{name}-genppd-nostatic.patch
Patch6:		%{name}-locale-names.patch
URL:		http://gimp-print.sourceforge.net/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
%{?with_cups:BuildRequires:	cups-devel >= 1.1.9}
BuildRequires:	docbook-style-dsssl
BuildRequires:	docbook-utils
BuildRequires:	gettext-devel
%{?with_ijs:BuildRequires:	ghostscript-ijs-devel}
%{?with_gimp:BuildRequires:	gimp-devel < 1.3}
%{?with_gimp:BuildRequires:	gimp-devel >= 1:1.2.3-1.4}
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	texinfo
BuildRequires:	texinfo-texi2dvi
# requred by texi2dvi when @image is used in .texi
BuildRequires:	tetex-dvips
BuildRequires:	tetex-format-plain
BuildRequires:	tetex-tex-misc
Requires:	%{name}-lib = %{version}
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

%description -l pl.UTF-8
Gimp-Print to zbiór bardzo wysokiej jakości sterowników do drukarek
dla systemów UNIX/Linux. Celem tego projektu jest jak najlepsza jakość
wydruku. Dołączone do tego pakietu są: wtyczka dla programu GIMP (stąd
nazwa), sterownik CUPS i sterownik Ghostscriptu. Sterownik umożliwia
bezpośrednią współpracę z wieloma kolejkami wydruku. Dodatkowo
dołączonych jest wiele programów do obsługi drukarki. Wielu
użytkowników twierdzi ze jakość wydruków na najlepszych drukarkach
Epson Stylus dorównuje albo nawet przerasta jakością to, co jest
oferowane przez sterowniki dla Windows i MacOS.

%description -l pt_BR.UTF-8
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
Summary(pl.UTF-8):   Biblioteka gimp-print
Summary(pt_BR.UTF-8):   Bibliotecas dinâmicas para impressão de alta qualidade
Group:		Libraries

%description lib
Gimp-print library.

%description lib -l pl.UTF-8
Biblioteka gimp-print.

%description lib -l pt_BR.UTF-8
Esse pacote contém bibliotecas dinâmicas de alta qualidade para serem
usados pelo plugin do Gimp gimp-print, pelo driver "stp" do
ghostscript e por drivers especializados do CUPS

%package devel
Summary:	gimp-print development tools
Summary(pl.UTF-8):   Pliki nagłówkowe itp. do gimp-print
Summary(pt_BR.UTF-8):   Cabeçalhos e arquivos de desenvolvimento para o libgimpprint
Group:		Development/Libraries
Requires:	%{name}-lib = %{version}-%{release}

%description devel
Gimp-print development tools and headers.

%description devel -l pl.UTF-8
Nagłówki i narzędzia deweloperskie dla Gimp-print.

%description devel -l pt_BR.UTF-8
Este são os arquivos de desenvolvimento para compilar programas com a
biblioteca libgimpprint.

%package static
Summary:	gimp-print static libraries
Summary(pl.UTF-8):   Statyczne biblioteki gimp-print
Summary(pt_BR.UTF-8):   Bibliotecas estáticas para desenvolvimento com gimp-print
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Gimp-print static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne Gimp-print.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com gimp-print.

%package -n escputil
Summary:	Tool for Epson ink printers
Summary(pl.UTF-8):   Narzędzie do drukarek atramentowych Epson
Summary(pt_BR.UTF-8):   Ferramenta de manutenção de impressoras ESPSON Stylus (R)
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

%description -n escputil -l pl.UTF-8
Działające z linii poleceń narzędzie dla drukarek atramentowych Epson.
Może być użyte do:
- oczyszczenia głowicy
- testu dysz
- wyrównania głowicy
- odczytu stanu drukarki
- odczytu ilości tuszu
- identyfikacji drukarki.

%description -n escputil -l pt_BR.UTF-8
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
Summary(pl.UTF-8):   gimp-print jako wtyczka do CUPS
Summary(pt_BR.UTF-8):   Entradas ppd para serem usadas com o cups
Group:		Applications/Printing
Requires:	%{name}-lib = %{version}-%{release}
Requires:	cups >= 1.1.9

%description cups
Gimp-print as CUPS plugin.

%description cups -l pl.UTF-8
Wtyczka gimp-print dla CUPS.

%description cups -l pt_BR.UTF-8
Este pacote contém os arquivos ppd para se usar o driver Gimp-Print
com o sistema de impressão cups.

%package samples
Summary:	gimp-print samples
Summary(pl.UTF-8):   Przykłady do gimp-print
Group:		Applications/Printing

%description samples
Gimp-print samples.

%description samples -l pl.UTF-8
Przykłady dla Gimp-print.

%package ijs
Summary:	gimp-print IJS driver for GhostScript
Summary(pl.UTF-8):   Sterownik IJS gimp-print dla GhostScripta
Group:		Applications/Printing

%description ijs
Gimp-print IJS driver for GhostScript.

%description ijs -l pl.UTF-8
Sterownik IJS Gimp-print dla GhostScript.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
#%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

# STP_PATH_GIMP
tail -n +4372 aclocal.m4 > scripts/stp-gimp.m4

%build
rm -f scripts/{gettext,libtool}.m4
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I scripts -I src/main
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with%{!?with_cups:out}-cups \
	--with%{!?with_gimp:out}-gimp \
	--with%{!?with_ijs:out}-ijs \
	--enable-escputil \
	--enable-libgimpprint \
	--without-foomatic \
	--with-samples \
	--with-user-guide \
	--without-ghost
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_datadir}/gimp-print/doc doc-installed
mv -f doc-installed/manual-html doc-installed/manual
mv -f doc-installed/html doc-installed/user-guide
mv -f $RPM_BUILD_ROOT%{_datadir}/gimp-print/samples \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	lib -p /sbin/ldconfig
%postun	lib -p /sbin/ldconfig

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%if %{with gimp}
%files
%defattr(644,root,root,755)
%attr(755,root,root) %(gimptool --gimpplugindir)/plug-ins/*
%endif

%files lib -f %{name}.lang
%defattr(644,root,root,755)
%doc doc-installed/*.pdf doc-installed/manual doc/FAQ.html AUTHORS README NEWS ChangeLog
%attr(755,root,root) %{_libdir}/libgimpprint.so.*.*.*
# XXX: conflict with libgimpprint-4.3.x (locales too...)
%{_mandir}/man7/gimpprint-*.7*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gimpprint-config
%attr(755,root,root) %{_libdir}/libgimpprint.so
%{_libdir}/libgimpprint.la
%{_includedir}/gimp-print
%{_aclocaldir}/gimpprint.m4
%{_mandir}/man1/gimpprint-config.1*
%{_mandir}/man3/gimpprint.3*
%{_infodir}/*info*

%files static
%defattr(644,root,root,755)
%{_libdir}/libgimpprint.a

%files -n escputil
%defattr(644,root,root,755)
%{_mandir}/man1/escputil.1*
%attr(755,root,root) %{_bindir}/escputil

%if %{with cups}
%files cups
%defattr(644,root,root,755)
%doc src/cups/README src/cups/command.txt src/cups/commands
%{_sysconfdir}/cups/command.types
%attr(755,root,root) %{_bindir}/cups-calibrate
%{_datadir}/cups/calibrate.ppm
%{_datadir}/cups/model/C/*
%{_datadir}/cups/model/en_GB/*
%lang(da) %{_datadir}/cups/model/da/*
%lang(fr) %{_datadir}/cups/model/fr/*
%lang(nb) %{_datadir}/cups/model/nb/*
%lang(pl) %{_datadir}/cups/model/pl/*
%lang(sv) %{_datadir}/cups/model/sv/*
%attr(755,root,root) %{_prefix}/lib/cups/backend/*
%attr(755,root,root) %{_prefix}/lib/cups/filter/*
%{_mandir}/man8/cups-calibrate.8*
%endif

%files samples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}

%if %{with ijs}
%files ijs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ijsgimpprint
%{_mandir}/man1/ijsgimpprint.1*
%endif
