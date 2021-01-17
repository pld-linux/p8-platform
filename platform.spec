Summary:	Platform support library used by libCEC and binary add-ons for Kodi
Name:		platform
Version:	2.1.0.1
Release:	1
License:	GPL v2+
Group:		Libraries
URL:		https://github.com/Pulse-Eight/platform/
Source0:	https://github.com/Pulse-Eight/platform/archive/p8-%{name}-%{version}.tar.gz
# Source0-md5:	3b9b00b7e0bb43532518741c1e30a2d7
BuildRequires:	cmake
BuildRequires:	libstdc++-devel

%description
Platform support library used by libCEC and binary add-ons for Kodi.

%package devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cmake

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n %{name}-p8-%{name}-%{version}

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_libdir}/libp8-%{name}.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libp8-%{name}.so.2

%files devel
%defattr(644,root,root,755)
%{_includedir}/p8-%{name}
%attr(755,root,root) %{_libdir}/libp8-%{name}.so
%{_libdir}/p8-%{name}
%{_pkgconfigdir}/p8-%{name}.pc
