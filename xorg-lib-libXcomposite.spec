Summary:	X Composite extension client library
Summary(pl.UTF-8):	Biblioteka kliencka rozszerzenia X Composite
Name:		xorg-lib-libXcomposite
Version:	0.4.6
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	https://xorg.freedesktop.org/releases/individual/lib/libXcomposite-%{version}.tar.xz
# Source0-md5:	af0a5f0abb5b55f8411cd738cf0e5259
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xmlto >= 0.0.20
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-proto-compositeproto-devel >= 0.4
BuildRequires:	xorg-proto-xproto-devel >= 7.0.22
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
Obsoletes:	libXcomposite < 1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Composite extension client library.

%description -l pl.UTF-8
Biblioteka kliencka rozszerzenia X Composite.

%package devel
Summary:	Header files for libXcomposite library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libXcomposite
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXfixes-devel
Requires:	xorg-proto-compositeproto-devel >= 0.4
Requires:	xorg-proto-xproto-devel >= 7.0.22
Obsoletes:	libXcomposite-devel < 1.1

%description devel
X Composite extension client library.

This package contains the header files needed to develop programs that
use libXcomposite.

%description devel -l pl.UTF-8
Biblioteka kliencka rozszerzenia X Composite.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libXcomposite.

%package static
Summary:	Static libXcomposite library
Summary(pl.UTF-8):	Biblioteka statyczna libXcomposite
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libXcomposite-static < 1.1

%description static
X Composite extension client library.

This package contains the static libXcomposite library.

%description static -l pl.UTF-8
Biblioteka kliencka rozszerzenia X Composite.

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
%doc AUTHORS COPYING ChangeLog README.md
%attr(755,root,root) %{_libdir}/libXcomposite.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libXcomposite.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXcomposite.so
%{_libdir}/libXcomposite.la
%{_includedir}/X11/extensions/Xcomposite.h
%{_pkgconfigdir}/xcomposite.pc
%{_mandir}/man3/XComposite*.3*
%{_mandir}/man3/Xcomposite.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXcomposite.a
