Summary:	gimp-print
Name:		gimp-print
Version:	4.2.0
Release:	0.1
Epoch:		0
License:	GPL
Group:		Applications/Printing
Source0:	%{name}-%{version}.tar.gz
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
gimp-print

%package lib
Summary: 	gimp-print library
Group: 		Libraries

%description lib
gimp-print library

%package devel
Summary:	gimp-print
Group:		Development/Libraries
Requires:	%{name}-lib = %{epoch}:%{version}-%{release}

%description devel
gimp-print

%package static
Summary:	gimp-print
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
gimp-print

%package -n escputil
Summary:	Tool for Epson ink printers
Group:		Applications/Printing

%description -n escputil
Tool for Epson ink printers

%package cups
Summary:	gimp-print as CUPS plugin
Group:		Applications/Printing

%description cups
gimp-print as CUPS plugin

%package samples
Summary:	gimp-print
Group:		Applications/Printing

%description samples
gimp-print

%package doc-html
Summary:	gimp-print
Group:		Applications/Printing

%description doc-html
gimp-print

%package doc-pdf
Summary:	gimp-print
Group:		Applications/Printing

%description doc-pdf
gimp-print

%package doc-ps
Summary:	gimp-print
Group:		Applications/Printing

%description doc-ps
gimp-print

%package manual-html
Summary:	gimp-print
Group:		Applications/Printing

%description manual-html
gimp-print


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
install -d $RPM_BUILD_ROOT/%{_examplesdir}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_datadir}/gimp-print/doc doc-installed
mv $RPM_BUILD_ROOT%{_datadir}/gimp-print/samples \
	$RPM_BUILD_ROOT/%{_examplesdir}/%{name}

gzip -9nf README ChangeLog

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post lib 
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1
/sbin/ldconfig

%postun lib 
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1
/sbin/ldconfig


%files 
%defattr(644,root,root,755)
%attr(755,root,root) %(gimptool --gimpplugindir)/plug-ins/*

%files lib -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgimpprint.so.1.0.0
%{_datadir}/info/*info*

%files devel
%defattr(644,root,root,755)
%{_includedir}/gimp-print
%{_aclocaldir}/gimpprint.m4
%{_mandir}/man1/gimpprint-config.1*z
%{_mandir}/man3/gimpprint.3*
%{_libdir}/libgimpprint.so
%{_libdir}/libgimpprint.la
%attr(755,root,root) %{_bindir}/gimpprint-config

%files static
%defattr(644,root,root,755)
%{_libdir}/libgimpprint.a

%files -n escputil
%defattr(644,root,root,755)
%{_mandir}/man1/escputil.1.gz
%attr(755,root,root) %{_bindir}/escputil


%files cups
%defattr(644,root,root,755)
%{_mandir}/man8/cups-calibrate.8.gz

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
%attr(755,root,root) %{_bindir}/cups-calibrate
%{_sysconfdir}/cups/command.types



%files samples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}

%files doc-html
%defattr(644,root,root,755)
%doc doc-installed/html

%files doc-pdf
%defattr(644,root,root,755)
%doc doc-installed/users-guide.pdf

%files manual-html
%defattr(644,root,root,755)
%doc doc-installed/manual-html

%files doc-ps
%defattr(644,root,root,755)
%doc doc-installed/gimpprint.ps
