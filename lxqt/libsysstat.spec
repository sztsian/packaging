Name:		libsysstat
Version:	0.4.1
Release:	1%{?dist}
License:	GPLv2 and LGPLv2+
Summary:	Library used to query system info and statistics
Url:		http://www.lxde.org
Source0:         https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires: 	%{?fedora:cmake >= 2.8.1}%{!?fedora:cmake3 >= 3.3}
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Help)
BuildRequires: lxqt-build-tools

%description
Library used to query system info and statistics

%package devel
Summary:	Devel files for libsysstat
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	pkgconfig

%description devel
Sysstat libraries for development.

%prep
%setup -q

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
	%{?fedora:%{cmake}}%{!?fedora:%{cmake3}} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc AUTHORS COPYING
%{_libdir}/libsysstat-qt5.so.*

%files devel
%dir %{_includedir}/sysstat-qt5/
%dir %{_datadir}/cmake/sysstat-qt5/
%{_includedir}/sysstat-qt5/*
%{_datadir}/cmake/sysstat-qt5/*
%{_libdir}/pkgconfig/sysstat-qt5.pc
%{_libdir}/libsysstat-qt5.so

%changelog
* Sat Aug 04 2018 Zamir SUN <zsun@fedoraproject.org> - 0.4.1-1
- Update to version 0.4.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Sep 25 2016 Helio Chissini de Castro <helio@kde.org> - 0.3.2-1
- New upstream release tied to lxqt 0.11

* Mon May 30 2016 Than Ngo <than@redhat.com> - 0.3.1-4
- cleanup

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 08 2015 Helio Chissini de Castro <helio@kde.org> - 0.3.1-2
- Prepare for lxqt epel7

* Mon Nov 02 2015 Helio Chissini de Castro <helio@kde.org> - 0.3.1-1
- New upstream version

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.3.0-3
- Rebuilt for GCC 5 C++11 ABI change

* Wed Feb 18 2015 Helio Chissini de Castro <helio@kde.org> - 0.3.0-2
- Rebuild (gcc5)

* Sun Feb 08 2015 Helio Chissini de Castro <helio@kde.org> - 0.3.0-1
- New upstream version 0.3.0

* Fri Oct 24 2014 TI_Eugene <ti.eugene@gmail.com> - 0.2.0-1
- Version bump
- qt5 only

* Fri Sep 26 2014 TI_Eugene <ti.eugene@gmail.com> - 0.1.0-1
- Initial packaging
