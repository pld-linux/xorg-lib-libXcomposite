Summary:	X Composite extension library
Summary(pl):	Biblioteka rozszerzenia X Composite
Name:		xorg-lib-libXcomposite
Version:	0.2.2.2
Release:	0.1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC4/lib/libXcomposite-%{version}.tar.bz2
# Source0-md5:	e4a4cda4c6bcf4fcfcf71f216590171d
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-proto-compositeproto-devel >= 0.2
BuildRequires:	xorg-util-util-macros
Obsoletes:	libXcomposite
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Composite extension library.

%description -l pl
Biblioteka rozszerzenia X Composite.

%package devel
Summary:	Header files for libXcomposite library
Summary(pl):	Pliki nag³ówkowe biblioteki libXcomposite
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXfixes-devel
Requires:	xorg-proto-compositeproto-devel >= 0.2
Obsoletes:	libXcomposite-devel

%description devel
X Composite extension library.

This package contains the header files needed to develop programs that
use libXcomposite.

%description devel -l pl
Biblioteka rozszerzenia X Composite.

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych biblioteki libXcomposite.

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

Pakiet zawiera statyczn± bibliotekê libXcomposite.

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

%files static
%defattr(644,root,root,755)
%{_libdir}/libXcomposite.a
