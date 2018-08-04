Name: libfm-qt
Version: 0.13.0
Release: 2%{?dist}
Summary: Companion library for PCManFM
License: GPLv2+
URL: http://lxqt.org
Source0: https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: pkgconfig(Qt5Help)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(libfm)
BuildRequires: pkgconfig(lxqt) >= 0.13.0
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: pkgconfig(libmenu-cache) >= 0.3.0
BuildRequires: libexif-devel
Requires: menu-cache-devel
Obsoletes: libfm-qt5 <  0.11.0
Obsoletes: libfm-qt4 <= 0.9.0
Obsoletes: libfm-qt-common <= 0.9.0
Provides: libfm-qt5 = %{version}

%description
Libfm-Qt is a companion library providing components to build
desktop file managers.

%package devel
Summary: Development files for libfm-qt
Requires: libfm-qt%{?_isa} = %{version}-%{release}
Obsoletes: libfm-qt-devel <= 0.9.0
Obsoletes: libfm-qt5-devel < 0.11.0
Obsoletes: libfm-qt4-devel <= 0.9.0
Provides: libfm-qt5-devel = %{version}

%description devel
libfm-qt-devel package contains libraries and header files for
developing applications that use libfm-qt.

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%prep
%setup -q

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
    %{cmake_lxqt} -DPULL_TRANSLATIONS=NO ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

# We need fix this upstream
find %{buildroot} -size 0 -delete

%files
%doc AUTHORS
%{_libdir}/libfm-qt.so.5*

%files devel
%{_libdir}/libfm-qt.so
%{_libdir}/pkgconfig/libfm-qt.pc
%{_includedir}/libfm-qt/
%dir %{_datadir}/cmake/fm-qt
%{_datadir}/cmake/fm-qt/*
%{_datadir}/libfm-qt/archivers.list
%{_datadir}/libfm-qt/terminals.list
%{_datadir}/mime/packages/libfm-qt-mimetypes.xml

%changelog
* Fri Aug 03 2018 Zamir SUN <zsun@fedoraproject.org> - 0.13.0-2
- Add menu-cache-devel as Require, otherwise cmake report 'Imported target "fm-qt" includes non-existent path'

* Fri Aug 03 2018 Zamir SUN <zsun@fedoraproject.org> - 0.13.0-1
- Update to version 0.13.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 21 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.11.2-13
- rebuild (qt5)

* Sun May 27 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.11.2-12
- rebuild (qt5)

* Wed Feb 14 2018 Jan Grulich <jgrulich@redhat.com> - 0.11.2-11
- rebuild (qt5)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 01 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.11.2-9
- rebuild (qt5)

* Sun Nov 26 2017 Rex Dieter <rdieter@fedoraproject.org> - 0.11.2-8
- rebuild (qt5)

* Wed Oct 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 0.11.2-7
- BR: qt5-qtbase-private-devel

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 19 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.2-3
- rebuilt

* Wed Jan 18 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.2-2
- moved translations to lxqt-l10n

* Mon Jan 16 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.2-1
- new version

* Thu Sep 29 2016 Helio Chissini de Castro <helio@kde.org> - 0.11.1-2
- Fix some rpmlint errors

* Mon Sep 26 2016 Helio Chissini de Castro <helio@kde.org> - 0.11.1-1
New package splitted from main pcmanfm-qt
