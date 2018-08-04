Name:    lxqt-config
Summary: Config tools for LXQt desktop suite
Version: 0.13.0
Release: 1%{?dist}
License: LGPLv2+
URL:     http://lxqt.org/
Source0: https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: %{?fedora:cmake}%{!?fedora:cmake3} >= 3.0
BuildRequires: pkgconfig(Qt5Help)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5Xdg) >= 2.0.0
BuildRequires: pkgconfig(lxqt) >= 0.13.0
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcursor)
BuildRequires: kf5-kwindowsystem-devel >= 5.5
BuildRequires: pkgconfig(kscreen2)
BuildRequires: desktop-file-utils

%description
%{summary}.

%prep
%setup -q

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
   %{cmake_lxqt} -DUSE_QT5=TRUE -DPULL_TRANSLATIONS=NO ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

for cfgapp in monitor input file-associations appearance cursor brightness locale; do
if [ -f %{buildroot}%{_datadir}/applications/lxqt-config-${cfgapp}.desktop ]; then
sed -i "/^GenericName.*/d" %{buildroot}%{_datadir}/applications/lxqt-config-${cfgapp}.desktop
sed -i "/^Comment.*/d" %{buildroot}%{_datadir}/applications/lxqt-config-${cfgapp}.desktop
desktop-file-edit \
    --remove-category=LXQt --add-category=X-LXQt \
    --remove-category=Help --add-category=X-Help \
    --remove-only-show-in=LXQt --add-only-show-in=X-LXQt \
    %{buildroot}%{_datadir}/applications/lxqt-config-${cfgapp}.desktop
fi
done
desktop-file-edit \
    --remove-category=LXQt --add-category=X-LXQt \
    --remove-category=Help --add-category=X-Help \
    --remove-only-show-in=LXQt --add-only-show-in=X-LXQt \
    %{buildroot}%{_datadir}/applications/lxqt-config.desktop


%files
%{_bindir}/lxqt-config
%{_bindir}/lxqt-config-brightness
%{_bindir}/lxqt-config-appearance
%{_bindir}/lxqt-config-file-associations
%{_bindir}/lxqt-config-input
%{_bindir}/lxqt-config-monitor
%{_bindir}/lxqt-config-locale
%{_datadir}/applications/lxqt-config-appearance.desktop
%{_datadir}/applications/lxqt-config-file-associations.desktop
%{_datadir}/applications/lxqt-config-input.desktop
%{_datadir}/applications/lxqt-config-monitor.desktop
%{_datadir}/applications/lxqt-config-locale.desktop
%{_datadir}/applications/lxqt-config.desktop
%{_datadir}/applications/lxqt-config-brightness.desktop
%{_libdir}/lxqt-config/liblxqt-config-cursor.so
%{_datadir}/icons/*/*
%{_datadir}/lxqt/icons/*
%config(noreplace) %{_sysconfdir}/xdg/menus/lxqt-config.menu

%changelog
* Fri Aug 03 2018 Zamir SUN <zsun@fedoraproject.org> - 0.13.0-1
- Update to version 0.13.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Oct 13 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.1-8
- Fix FTBFS (cmake): https://github.com/lxde/lxqt/issues/1277

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 19 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.1-4
- rebuilt

* Wed Jan 18 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.1-3
- moved translations to lxqt-l10n

* Wed Jan 11 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.1-2
- Doesn't build on epel7 with aarch64

* Sat Jan 07 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.1-1
- new version

* Thu Sep 29 2016 Helio Chissini de Castro <helio@kde.org> - 0.11.0-2
- Fix rpmlint issues

* Sun Sep 25 2016 Helio Chissini de Castro <helio@kde.org> - 0.11.0-1
- New upstream version 0.11.0

* Mon Apr 11 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.10.0-6
- rebuild

* Mon Apr 11 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.10.0-5
- rebuild (kscreen2)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Helio Chissini de Castro <helio@kde.org> - 0.10.0-3
- Remove razorqt conflicts

* Wed Dec 09 2015 Helio Chissini de Castro <helio@kde.org> - 0.10.0-2
- Use new cmake_lxqt macro to enable epel 7

* Mon Nov 02 2015 Helio Chissini de Castro <helio@kde.org> - 0.10.0-1
- New upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.0-5
- Rebuilt for GCC 5 C++11 ABI change

* Wed Feb 18 2015 Helio Chissini de Castro <helio@kde.org> - 0.9.0-4
- Rebuild (gcc5)

* Tue Feb 10 2015 Helio Chissini de Castro <helio@kde.org> - 0.9.0-3
- Obsoletes razorqt-config as migrated to lxqt

* Mon Feb 09 2015 Helio Chissini de Castro <helio@kde.org> - 0.9.0-2
- Proper add locale for Qt tm files

* Sun Feb 08 2015 Helio Chissini de Castro <helio@kde.org> - 0.9.0-1
- New upstream release 0.9.0

* Tue Feb 03 2015 Helio Chissini de Castro <hcastro@redhat.com> - 0.9.0-0.1
- Preparing for 0.9.0 release

* Mon Dec 29 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-5
- Rebuild against new Qt 5.4.0

* Sun Dec 21 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-4
- Unify naming as discussed on Fedora IRC

* Mon Nov 10 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-3
- Update on review https://bugzilla.redhat.com/show_bug.cgi?id=1159882

* Mon Nov 03 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-2
- Update to Fedora package review 

* Mon Oct 27 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-1
- First release to LxQt new base
