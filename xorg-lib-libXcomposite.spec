Summary:	X Composite extension library
Summary(pl):	Biblioteka rozszerzenia X Composite
Name:		xorg-lib-libXcomposite
Version:	0.2.0
Release:	0.03
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/lib/libXcomposite-%{version}.tar.bz2
# Source0-md5:	906dad7523e8797e25c0874223292357
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-proto-compositeproto-devel
BuildRequires:	xorg-util-util-macros
Obsoletes:	libXcomposite
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
X Composite extension library.

%description -l pl
Biblioteka rozszerzenia X Composite.

%package devel
Summary:	Header files libXcomposite development
Summary(pl):	Pliki nagłówkowe do biblioteki libXcomposite
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXfixes-devel
Requires:	xorg-proto-compositeproto-devel
Obsoletes:	libXcomposite-devel

%description devel
X Composite extension library.

This package contains the header files needed to develop programs that
use these libXcomposite.

%description devel -l pl
Biblioteka rozszerzenia X Composite.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libXcomposite.

%package static
Summary:	Static libXcomposite library
Summary(pl):	Biblioteka statyczna libXcomposite
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libXcomposite-static

%description static
X Composite extension library.

This package contains the static libXcomposite library.

%description static -l pl
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
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/libXcomposite.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXcomposite.so
%{_libdir}/libXcomposite.la
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/xcomposite.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libXcomposite.a
