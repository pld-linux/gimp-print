Summary:	Collection of high-quality printer drivers
Name:		gimp-print
Version:	4.2.0
Release:	0.1
License:	GPL
Group:		Applications/Printing
Group(de):	Applikationen/Drucken
Group(es):	Aplicaciones/Impresión
Group(fr):	Applications/Impression
Group(pl):	Aplikacje/Drukowanie
Group(pt):	Aplicações/Impressão
Source0:	http://prdownloads.sourceforge.net/gimp-print/%{name}-%{version}.tar.gz
Patch0:		%{name}-install.patch
URL:		http://gimp-print.sf.net/
BuildRequires:	gimp-devel >= 1:1.2.2-4
BuildRequires:	cups-devel >= 1.1.9
BuildRequires:	/usr/bin/texi2html
BuildRequires:	tetex-dvips
BuildRequires:	/usr/bin/db2html
BuildRequires:	/usr/bin/db2ps
BuildRequires:	/usr/bin/db2pdf
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
Epson Stylus dorównuje albo nawet przerasta jako¶ci± to co jest
oferowane przez sterowniki dla Windows i MacOS

%package lib
Summary:	gimp-print library
Summary(pl):	Biblioteka Gimp-print
Group:		Libraries
Group(de):	Bibliotheken
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt):	Bibliotecas
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ

%description lib
Gimp-print library.

%description -l pl
Biblioteka Gimp-print.

%package devel
Summary:	gimp-print development tools
Group:		Development/Libraries
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(pt):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name}-lib = %{version}-%{release}

%description devel
Gimp-print development tools and headers.

%description -l pl devel
Nag³ówki i narzêdzia deweloperskie dla Gimp-print.

%package static
Summary:	gimp-print static libraries
Group:		Development/Libraries
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(pt):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name}-devel = %{version}-%{release}

%description static
Gimp-print static libraries.

%description -l pl
Biblioteki statyczne Gimp-print.

%package -n escputil
Summary:	Tool for Epson ink printers
Group:		Applications/Printing
Group(de):	Applikationen/Drucken
Group(es):	Aplicaciones/Impresión
Group(fr):	Applications/Impression
Group(pl):	Aplikacje/Drukowanie
Group(pt):	Aplicações/Impressão

%description -n escputil
Tool for Epson ink printers.

%description -l pl -n escputil
Narzêdzie dla drukarek atramentowych Epson.

%package cups
Summary:	gimp-print as CUPS plugin
Group:		Applications/Printing
Group(de):	Applikationen/Drucken
Group(es):	Aplicaciones/Impresión
Group(fr):	Applications/Impression
Group(pl):	Aplikacje/Drukowanie
Group(pt):	Aplicações/Impressão
Requires:	cups >= 1.1.9

%description cups
Gimp-print as CUPS plugin.

%description -l pl cups
Plugin gimp-print dla CUPS.

%package samples
Summary:	gimp-print samples
Group:		Applications/Printing
Group(de):	Applikationen/Drucken
Group(es):	Aplicaciones/Impresión
Group(fr):	Applications/Impression
Group(pl):	Aplikacje/Drukowanie
Group(pt):	Aplicações/Impressão

%description samples
Gimp-print samples.

%description -l pl samples
Przyk³ady dla Gimp-print.

%prep
%setup  -q
%patch0 -p1

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

mv $RPM_BUILD_ROOT%{_datadir}/gimp-print/doc doc-installed
mv doc-installed/manual-html doc-installed/manual
mv doc-installed/html doc-instlled/user-guide
mv $RPM_BUILD_ROOT%{_datadir}/gimp-print/samples \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}

gzip -9nf README ChangeLog AUTHORS README NEWS

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post lib -p /sbin/ldconfig

%postun lib -p /sbin/ldconfig

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
%{_libdir}/cups/backend/epson
%{_libdir}/cups/backend/canon
%{_libdir}/cups/filter/rastertoprinter
%{_libdir}/cups/filter/commandtoepson
%{_libdir}/cups/filter/commandtocanon
%{_mandir}/man8/cups-calibrate.8*

%files samples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}
