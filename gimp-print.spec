#
# Conditional build:
# _without_cups		- without CUPS subpackage
# _without_gimp		- without GIMP plugin subpackage
# _without_ijs		- without IJS server for Ghostscript
#
# TODO:
# - port info_and_pdf_only.patch and install documentation in correct place.
# - port install.patch (afect only gimp plugin)
# - port info.patch (if needed)
# - think about not including PPDs in package and allow generation by cups-genppd
#
%include	/usr/lib/rpm/macros.perl
Summary:	Collection of high-quality printer drivers
Summary(pl):	Zestaw wysokiej jako�ci sterownik�w do drukarek
Summary(pt_BR):	plugin GIMP-Print para impress�o de imagens em alta qualidade
Name:		gimp-print
Version:	4.3.5
Release:	1
License:	GPL
Group:		Applications/Printing
Source0:	http://prdownloads.sourceforge.net/gimp-print/%{name}-%{version}.tar.bz2
Patch0:		%{name}-install.patch
Patch1:		%{name}-info.patch
Patch2:		%{name}-usb.patch
Patch3:		%{name}-info_and_pdf_only.patch
URL:		http://gimp-print.sf.net/
%{!?_without_cups:BuildRequires:	cups-devel >= 1.1.9}
%{!?_without_gimp:BuildRequires:	gimp-devel >= 1:1.2.3-1.4}
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	texinfo
BuildRequires:	texinfo-texi2dvi
BuildRequires:	docbook-style-dsssl
BuildRequires:	docbook-utils
%{!?_without_ijs:BuildRequires:	ghostscript-ijs-devel}
BuildRequires:	rpm-perlprov >= 3.0.3-16
Requires:	gimp >= 1:1.2.2-5
Requires:	%{name}-lib = %{version}
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
Gimp-Print to zbi�r bardzo wysokiej jako�ci sterownik�w do drukarek
dla system�w UNIX/Linux. Celem tego projektu jest jak najlepsza jako��
wydruku. Do��czone do tego pakietu s�: wtyczka dla programu GIMP (st�d
nazwa), sterownik CUPS i sterownik Ghostscriptu. Sterownik umo�liwia
bezpo�redni� wsp�prac� z wieloma kolejkami wydruku. Dodatkowo
do��czonych jest wiele program�w do obs�ugi drukarki. Wielu
u�ytkownik�w twierdzi ze jako�� wydruk�w na najlepszych drukarkach
Epson Stylus dor�wnuje albo nawet przerasta jako�ci� to, co jest
oferowane przez sterowniki dla Windows i MacOS.

%description -l pt_BR
Este � um plugin para o Gimp que permite a impress�o de imagens e
fotos em uma qualidade muito boa em v�rias impressoras de jato de
tinta modernas e em algumas lasers. Especialmente nas impressoras
Epsion Stylus a qualidade se equipara a mesma obtida em sistema
operacionais propriet�rios, uma vez que a Epson publicou as
especifica��es dos protocolos usados por suas impressoras. Outras
marcas de impressoras como HP tamb�m atingem qualidades altas de
impress�o. Esse plugin tamb�m � capaz de gerar arquivos Postscript que
permite ser usado em qualquer outra impressora.

%package lib
Summary:	gimp-print library
Summary(pl):	Biblioteka gimp-print
Summary(pt_BR):	Bibliotecas din�micas para impress�o de alta qualidade
Group:		Libraries

%description lib
Gimp-print library.

%description lib -l pl
Biblioteka Gimp-print.

%description lib -l pt_BR
Esse pacote cont�m bibliotecas din�micas de alta qualidade para serem
usados pelo plugin do Gimp gimp-print, pelo driver "stp" do
ghostscript e por drivers especializados do CUPS

%package devel
Summary:	gimp-print development tools
Summary(pl):	Pliki nag��wkowe itp. do gimp-print
Summary(pt_BR):	Cabe�alhos e arquivos de desenvolvimento para o libgimpprint
Group:		Development/Libraries
Requires:	%{name}-lib = %{version}-%{release}

%description devel
Gimp-print development tools and headers.

%description devel -l pl
Nag��wki i narz�dzia deweloperskie dla Gimp-print.

%description devel -l pt_BR
Este s�o os arquivos de desenvolvimento para compilar programas com a
biblioteca libgimpprint.

%package static
Summary:	gimp-print static libraries
Summary(pl):	Statyczne biblioteki gimp-print
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com gimp-print
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Gimp-print static libraries.

%description static -l pl
Biblioteki statyczne Gimp-print.

%description static -l pt_BR
Bibliotecas est�ticas para desenvolvimento com gimp-print.

%package -n escputil
Summary:	Tool for Epson ink printers
Summary(pl):	Narz�dzie do drukarek atramentowych Epson
Summary(pt_BR):	Ferramenta de manuten��o de impressoras ESPSON Stylus (R)
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
Dzia�aj�ce z linii polece� narz�dzie dla drukarek atramentowych Epson.
Mo�e by� u�yte do:
- oczyszczenia g�owicy
- testu dysz
- wyr�wnania g�owicy
- odczytu stanu drukarki
- odczytu ilo�ci tuszu
- identyfikacji drukarki.

%description -n escputil -l pt_BR
Ferramenta de manuten��o de impressoras ESPSON Stylus (R). Esta
ferramenta de linha de comando � usada para executar as seguintes
tarefas:
- Limpeza de cabe�ote
- Checagem de Qualidade de impress�o
- Alinhamento de cabe�ote
- Estado da Impressora
- N�vel de tinta
- Identifica��o da Impressora

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
Este pacote cont�m os arquivos ppd para se usar o driver Gimp-Print
com o sistema de impress�o cups.

%package samples
Summary:	gimp-print samples
Summary(pl):	Przyk�ady do gimp-print
Group:		Applications/Printing

%description samples
Gimp-print samples.

%description samples -l pl
Przyk�ady dla Gimp-print.

%package ijs
Summary:	gimp-print IJS driver for GhostScript
Summary(pl):	Sterownik IJS Gimp-print dla GhostScript
Group:		Applications/Printing

%description ijs
Gimp-print IJS driver for GhostScript.

%description ijs -l pl
Sterownik IJS Gimp-print dla GhostScript.


%prep 
%setup  -q 
#%patch0 -p1
#%patch1 -p1
%patch2 -p1
#%patch3 -p1

%build
%configure \
	%{?debug:--enable-debug} \
	--with%{?_without_cups:out}-cups \
	--with%{?_without_gimp:out}-gimp \
	--with%{?_without_ijs:out}-ijs \
	--enable-escputil \
	--enable-libgimpprint \
	--enable-translated-cups-ppds \
	--enable-cups-level3-ppds \
	--enable-lexmarkutil \
	--without-foomatic \
	--enable-samples \
	--enable-user-guide \
	--enable-static \
	--without-ghost
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

#mv -f $RPM_BUILD_ROOT%{_datadir}/gimp-print/doc doc-installed
#mv -f doc-installed/manual-html doc-installed/manual
#mv -f doc-installed/html doc-installed/user-guide
mv -f $RPM_BUILD_ROOT%{_datadir}/gimp-print/samples \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}
rm -f $RPM_BUILD_ROOT%{_mandir}/man8/update-cups-genppd.8
echo '.so cups-genppdconfig.8' > $RPM_BUILD_ROOT%{_mandir}/man8/update-cups-genppd.8

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	lib -p /sbin/ldconfig
%postun	lib -p /sbin/ldconfig

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%if %{?!_without_gimp:1}%{?_without_gimp:0}
%files
%defattr(644,root,root,755)
%attr(755,root,root) %(gimptool --gimpplugindir)/plug-ins/*
%endif

%files lib -f %{name}.lang
%defattr(644,root,root,755)
#%%doc doc-installed/*.pdf doc-installed/manual 
%doc doc/FAQ.html AUTHORS README NEWS ChangeLog
%attr(755,root,root) %{_libdir}/libgimpprint-*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgimpprint.so
%{_libdir}/libgimpprint.la
%attr(755,root,root) %{_bindir}/gimpprint-config
%{_includedir}/gimp-print
%{_aclocaldir}/gimpprint.m4
%{_pkgconfigdir}/*
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

%if %{?_without_cups:0}%{!?_without_cups:1}
%files cups
%defattr(644,root,root,755)
%doc src/cups/README src/cups/command.txt src/cups/commands
%{_sysconfdir}/cups/command.types
%attr(755,root,root) %{_bindir}/cups-*
%{_datadir}/cups/calibrate.ppm
#%{_datadir}/cups/model/C/*
%{_datadir}/cups/model/gimp-print/en/*
%lang(en_GB) %{_datadir}/cups/model/gimp-print/en_GB/*
%lang(da) %{_datadir}/cups/model/gimp-print/da/*
%lang(de) %{_datadir}/cups/model/gimp-print/de/*
%lang(el) %{_datadir}/cups/model/gimp-print/el/*
%lang(es) %{_datadir}/cups/model/gimp-print/es/*
%lang(fr) %{_datadir}/cups/model/gimp-print/fr/*
%lang(nl) %{_datadir}/cups/model/gimp-print/nl/*
%lang(no) %{_datadir}/cups/model/gimp-print/no/*
%lang(pl) %{_datadir}/cups/model/gimp-print/pl/*
%lang(pt) %{_datadir}/cups/model/gimp-print/pt/*
%lang(sk) %{_datadir}/cups/model/gimp-print/sk/*
%lang(sv) %{_datadir}/cups/model/gimp-print/sv/*
%attr(755,root,root) %{_libdir}/cups/backend/*
%attr(755,root,root) %{_libdir}/cups/filter/*
%{_mandir}/man8/*cups*.8*
%endif

%files samples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}

%if %{?_without_ijs:0}%{!?_without_ijs:1}
%files ijs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ijsgimpprint
%endif
