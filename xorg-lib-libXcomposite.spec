Summary:	X Composite extension library
Summary(pl.UTF-8):	Biblioteka rozszerzenia X Composite
Name:		xorg-lib-libXcomposite
Version:	0.4.1
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXcomposite-%{version}.tar.bz2
# Source0-md5:	0f1367f57fdf5df17a8dd71d0fa68248
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-proto-compositeproto-devel >= 0.4
BuildRequires:	xorg-util-util-macros
Obsoletes:	libXcomposite
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Composite extension library.

%description -l pl.UTF-8
Biblioteka rozszerzenia X Composite.

%package devel
Summary:	Header files for libXcomposite library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libXcomposite
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXfixes-devel
Requires:	xorg-proto-compositeproto-devel >= 0.4
Obsoletes:	libXcomposite-devel

%description devel
X Composite extension library.

This package contains the header files needed to develop programs that
use libXcomposite.

%description devel -l pl.UTF-8
Biblioteka rozszerzenia X Composite.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libXcomposite.

%package static
Summary:	Static libXcomposite library
Summary(pl.UTF-8):	Biblioteka statyczna libXcomposite
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libXcomposite-static

%description static
X Composite extension library.

This package contains the static libXcomposite library.

%description static -l pl.UTF-8
Biblioteka rozszerzenia X Composite.

Pakiet zawiera statyczną bibliotekę libXcomposite.

%prep
%setup -q -n libXcomposite-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog
%attr(755,root,root) %{_libdir}/libXcomposite.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXcomposite.so
%{_libdir}/libXcomposite.la
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/xcomposite.pc
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXcomposite.a
