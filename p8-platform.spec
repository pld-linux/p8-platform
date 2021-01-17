Summary:	Platform support library used by libCEC and binary add-ons for Kodi
Name:		p8-platform
Version:	2.1.0.1
Release:	1
License:	GPL v2+
Group:		Libraries
URL:		https://github.com/Pulse-Eight/platform/
Source0:	https://github.com/Pulse-Eight/platform/archive/%{name}-%{version}.tar.gz
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
%setup -q -n platform-p8-platform-%{version}

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
%attr(755,root,root) %{_libdir}/lib%{name}.so.*.*
%attr(755,root,root) %ghost %{_libdir}/lib%{name}.so.2

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
%attr(755,root,root) %{_libdir}/lib%{name}.so
%{_libdir}/%{name}
%{_pkgconfigdir}/%{name}.pc
