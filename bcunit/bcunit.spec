Name:           BCUnit
Version:        3.0.2
Release:        1%{?dist}
Summary:        A fork of the defunct project CUnit (see below), with several fixes and patches applied.
License:        GPLv2+
URL:            https://github.com/BelledonneCommunications/bcunit
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  autoconf

%description
A fork of the defunct project CUnit (see below), with several fixes and patches applied.

%package        devel
Summary:        Development files for bcunit
Requires:       %{name} = %{version}-%{release}

%description devel
A fork of the defunct project CUnit (see below), with several fixes and patches applied.

%prep
%setup -q -n bcunit-%{version}

%build
autoreconf -vfi
%configure

make 

%install
%make_install PREFIX="%{_prefix}"
find $RPM_BUILD_ROOT -name \*.la -exec rm {} \;
mv %{buildroot}%{_prefix}/doc %{buildroot}%{_datadir}/doc

%files
%doc README
%license COPYING
%{_datadir}/BCUnit/
%{_datadir}/doc/%{name}
%{_mandir}/man3/%{name}.3.gz

%files devel
%{_includedir}/BCUnit
%{_libdir}/libbcunit.so*
%{_libdir}/pkgconfig/bcunit.pc

%changelog
* Sun Aug 06 2017 Zamir SUN <sztsian@gmail.com> - 2.2.14-2
- Remove group tag
- Fix rpmlint shebang error
