Name:       pavucontrol-qt
Version:    0.4.0
Release:    1%{?dist}
License:    GPLv2+
URL:        http://lxqt.org/
Source0:    https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

Summary:    Qt port of volume control pavucontrol
Patch0:     pavucontrol-qt-0.1.0-naming.patch
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  qt5-linguist
BuildRequires:  pkgconfig(lxqt) >= 0.13.0
BuildRequires:  pkgconfig(Qt5Xdg) >= 2.0.0
BuildRequires:  pkgconfig(libpulse) >= 5.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.0

%description
%{summary}

%prep
%setup -q
%patch0 -p1

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
    %{cmake_lxqt} \
    -DPULL_TRANSLATIONS=NO ..
popd

%make_build -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop


%files
%license LICENSE
%doc AUTHORS
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop

%changelog
* Sat Aug 04 2018 Zamir SUN <zsun@fedoraproject.org> - 0.4.0-1
- Update to version 0.4.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.2.0-7
- BR: gcc-c++, use %%make_build

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 19 2017 Christian Dersch <lupinix@mailbox.org> - 0.2.0-3
- rebuilt

* Wed Jan 18 2017 Christian Dersch <lupinix@mailbox.org> - 0.2.0-2
- moved translations to lxqt-l10n

* Wed Jan 11 2017 Christian Dersch <lupinix@mailbox.org> - 0.2.0-1
- new version

* Tue Sep 27 2016 Helio Chissini de Castro <helio@kde.org> - 0.1.0-2
- Change a bit the naming patch to use similar one upstreamed

* Mon Sep 26 2016 Helio Chissini de Castro <helio@kde.org> - 0.1.0-1
- New package. Distributed tied to lxqt 0.11.0 release
