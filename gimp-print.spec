#
# Conditional build:
%bcond_without	cups		# don't build CUPS plugin
%bcond_without	gimp		# build GIMP plugin subpackage
%bcond_without	ijs		# don't build IJS server for Ghostscript
%bcond_without	foomatic	# don't generate foomatic data
%bcond_without	static_libs	# don't build static libraries
#
# TODO:
# - port info_and_pdf_only.patch and install documentation in correct place.
# - think about not including PPDs in package and allow generation by cups-genppd
#
%include	/usr/lib/rpm/macros.perl
Summary:	Collection of high-quality printer drivers
Summary(pl):	Zestaw wysokiej jako�ci sterownik�w do drukarek
Summary(pt_BR):	plugin GIMP-Print para impress�o de imagens em alta qualidade
Name:		gimp-print
Version:	5.0.0
%define	bver	beta1
Release:	0.%{bver}.1
License:	GPL
Group:		Applications/Printing
Source0:	http://dl.sourceforge.net/gimp-print/%{name}-%{version}-%{bver}.tar.bz2
# Source0-md5:	67d211692385458602400b65b34cefe8
#Patch0:		%{name}-info.patch
Patch0:		%{name}-usb.patch
Patch1:		%{name}-opt.patch
Patch2:		%{name}-locale-names.patch
URL:		http://gimp-print.sf.net/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
%{?with_cups:BuildRequires:	cups-devel >= 1.1.15}
BuildRequires:	docbook-style-dsssl
BuildRequires:	docbook-utils
%{?with_foomatic:BuildRequires:	foomatic-db-engine >= 2.9.1}
BuildRequires:	gettext-autopoint
%{?with_ijs:BuildRequires:	ghostscript-ijs-devel}
%{?with_gimp:BuildRequires:	gimp-devel >= 1:2.0.0}
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	texinfo
BuildRequires:	texinfo-texi2dvi
Requires:	gimp >= 1:1.2.2-5
Requires:	libgimpprint = %{version}-%{release}
Conflicts:	gimp > 1:1.3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		gimpplugindir	%(gimptool --gimpplugindir)/plug-ins

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

%package -n libgimpprint
Summary:	gimp-print library
Summary(pl):	Biblioteka gimp-print
Summary(pt_BR):	Bibliotecas din�micas para impress�o de alta qualidade
Group:		Libraries
Obsoletes:	gimp-print-lib

%description -n libgimpprint
Gimp-print library.

%description -n libgimpprint -l pl
Biblioteka Gimp-print.

%description -n libgimpprint -l pt_BR
Esse pacote cont�m bibliotecas din�micas de alta qualidade para serem
usados pelo plugin do Gimp gimp-print, pelo driver "stp" do
ghostscript e por drivers especializados do CUPS

%package -n libgimpprint-devel
Summary:	gimp-print development tools
Summary(pl):	Pliki nag��wkowe itp. do gimp-print
Summary(pt_BR):	Cabe�alhos e arquivos de desenvolvimento para o libgimpprint
Group:		Development/Libraries
Requires:	libgimpprint = %{version}-%{release}
Obsoletes:	gimp-print-devel

%description -n libgimpprint-devel
Gimp-print development tools and headers.

%description -n libgimpprint-devel -l pl
Nag��wki i narz�dzia deweloperskie dla Gimp-print.

%description -n libgimpprint-devel -l pt_BR
Este s�o os arquivos de desenvolvimento para compilar programas com a
biblioteca libgimpprint.

%package -n libgimpprint-static
Summary:	gimp-print static libraries
Summary(pl):	Statyczne biblioteki gimp-print
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com gimp-print
Group:		Development/Libraries
Requires:	libgimpprint-devel = %{version}-%{release}
Obsoletes:	gimp-print-static

%description -n libgimpprint-static
Gimp-print static libraries.

%description -n libgimpprint-static -l pl
Biblioteki statyczne Gimp-print.

%description -n libgimpprint-static -l pt_BR
Bibliotecas est�ticas para desenvolvimento com gimp-print.

%package -n libgimpprintui
Summary:	gimp-print UI library
Summary(pl):	Biblioteka gimp-print
Summary(pt_BR):	Bibliotecas din�micas para impress�o de alta qualidade
Group:		Libraries
Requires:	libgimpprint = %{version}-%{release}

%description -n libgimpprintui
Gimp-print library.

%description -n libgimpprintui -l pl
Biblioteka Gimp-print.

%description -n libgimpprintui -l pt_BR
Esse pacote cont�m bibliotecas din�micas de alta qualidade para serem
usados pelo plugin do Gimp gimp-print, pelo driver "stp" do
ghostscript e por drivers especializados do CUPS

%package -n libgimpprintui-devel
Summary:	gimp-print development tools
Summary(pl):	Pliki nag��wkowe itp. do gimp-print
Summary(pt_BR):	Cabe�alhos e arquivos de desenvolvimento para o libgimpprint
Group:		Development/Libraries
Requires:	libgimpprintui = %{version}-%{release}
Requires:	libgimpprint-devel = %{version}-%{release}

%description -n libgimpprintui-devel
Gimp-print development tools and headers.

%description -n libgimpprintui-devel -l pl
Nag��wki i narz�dzia deweloperskie dla Gimp-print.

%description -n libgimpprintui-devel -l pt_BR
Este s�o os arquivos de desenvolvimento para compilar programas com a
biblioteca libgimpprint.

%package -n libgimpprintui-static
Summary:	gimp-print static libraries
Summary(pl):	Statyczne biblioteki gimp-print
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com gimp-print
Group:		Development/Libraries
Requires:	libgimpprintui-devel = %{version}-%{release}

%description -n libgimpprintui-static
Gimp-print static libraries.

%description -n libgimpprintui-static -l pl
Biblioteki statyczne Gimp-print.

%description -n libgimpprintui-static -l pt_BR
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
Requires:	libgimpprint = %{version}-%{release}
Requires:	cups >= 1.1.15

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
%setup -q -n %{name}-%{version}-%{bver}
%patch0 -p1
%patch1 -p1
%patch2 -p1

mv -f po/{no,nb}.po

echo 'AC_DEFUN([AM_PATH_GTK],[$3])' > m4/gtk.m4

%build
rm -f m4extra/{libtool.m4,gettext.m4,lcmessage.m4,progtest.m4}
%{?with_gimp:rm -f m4extra/gimp.m4}
%{__libtoolize}
%{__autopoint}
%{__aclocal} -I m4 -I m4extra
%{__automake}
%{__autoconf}

%configure \
	%{?debug:--enable-debug} \
	--with%{!?with_cups:out}-cups \
	--without-gimp \
	--with%{!?with_gimp:out}-gimp2 \
	--with%{!?with_ijs:out}-ijs \
	--with%{!?with_foomatic:out}-foomatic \
	%{?with_static_libs:--enable-static} \
	--with-modules=dlopen \
	--enable-escputil \
	--enable-libgimpprint \
	%{!?with_cups:--disable-cups-ppds} \
	--disable-libgimpprintui \
	--disable-static-genppd \
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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
%if %{with gimp}
	gimp_plug_indir=%{gimpplugindir}
%endif

mv -f $RPM_BUILD_ROOT%{_datadir}/gimp-print/doc doc-installed
#mv -f doc-installed/manual-html doc-installed/manual
#mv -f doc-installed/html doc-installed/user-guide
mv -f $RPM_BUILD_ROOT%{_datadir}/gimp-print/samples \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}

%if %{with cups}
rm -f $RPM_BUILD_ROOT%{_mandir}/man8/update-cups-genppd.8
echo '.so cups-genppdconfig.8' > $RPM_BUILD_ROOT%{_mandir}/man8/update-cups-genppd.8
%endif

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/%{version}*/modules/*.{a,la}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n libgimpprint -p /sbin/ldconfig
%postun	-n libgimpprint -p /sbin/ldconfig

%post	-n libgimpprintui -p /sbin/ldconfig
%postun	-n libgimpprintui -p /sbin/ldconfig

%if %{with gimp}
%files
%defattr(644,root,root,755)
%attr(755,root,root) %{gimpplugindir}/*
%endif

%files -n libgimpprint -f %{name}.lang
%defattr(644,root,root,755)
%doc doc-installed/gimpprint.pdf doc-installed/html doc-installed/users-guide.pdf
%doc doc/FAQ.html AUTHORS README NEWS ChangeLog
%attr(755,root,root) %{_libdir}/libgimpprint-*.so
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/%{version}*
%dir %{_libdir}/%{name}/%{version}*/modules
%attr(755,root,root) %{_libdir}/%{name}/%{version}*/modules/*.so
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/%{version}*
%{_mandir}/man7/*

%files -n libgimpprint-devel
%defattr(644,root,root,755)
%doc doc-installed/reference-html
%attr(755,root,root) %{_libdir}/libgimpprint.so
%{_libdir}/libgimpprint.la
%{_includedir}/gimp-print
%{_pkgconfigdir}/gimpprint.pc
%{_mandir}/man3/gimpprint.3*

%if %{with static_libs}
%files -n libgimpprint-static
%defattr(644,root,root,755)
%{_libdir}/libgimpprint.a
%endif

%files -n libgimpprintui
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgimpprintui2-*.so

%files -n libgimpprintui-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgimpprintui2.so
%{_libdir}/libgimpprintui2.la
%{_includedir}/gimp-print-ui2
%{_pkgconfigdir}/gimpprintui2.pc

%if %{with static_libs}
%files -n libgimpprintui-static
%defattr(644,root,root,755)
%{_libdir}/libgimpprintui2.a
%endif

%files -n escputil
%defattr(644,root,root,755)
%{_mandir}/man1/escputil.1*
%attr(755,root,root) %{_bindir}/escputil

%if %{with cups}
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
#%lang(nb) %{_datadir}/cups/model/gimp-print/nb/*
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

%if %{with ijs}
%files ijs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ijsgimpprint
%{_mandir}/man1/ijsgimpprint.1*
%endif

%if %{with foomatic}
%files -n foomatic-db-gimp-print
%defattr(644,root,root,755)
%{_datadir}/foomatic/db/source/driver/*
%{_datadir}/foomatic/db/source/opt/*
%endif
