Name:    lxqt-sudo
Version: 0.13.0
Release: 1%{?dist}
Summary: GUI frontend for sudo/su
License: LGPLv2+
URL:     http://lxqt.org/
Source0: https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: %{?fedora:cmake}%{!?fedora:cmake3} >= 3.0
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(lxqt) >= 0.13.0
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: qt5-linguist
Requires: sudo

%description
%{summary}.

%prep
%autosetup -p1

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
    %{cmake_lxqt} -DPULL_TRANSLATIONS=NO ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

#for desktop in %{buildroot}/%{_datadir}/lxqt/lxqt-panel/*.desktop; do
    # Exclude category as been Service 
#    desktop-file-edit --remove-category=LXQt --remove-only-show-in=LXQt --add-only-show-in=X-LXQt ${desktop}
#done


%files
%license LICENSE
%doc AUTHORS
%{_bindir}/lx*
%{_mandir}/man1/lx*.1*

%changelog
* Fri Aug 03 2018 Zamir SUN <zsun@fedoraproject.org> - 0.13.0-1
- Update to version 0.13.0

* Tue Jul 17 2018 Raphael Groner <projects.rg@smart.ms> - 0.11.1-9
- add patch for Qt5.11 header

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 19 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.1-3
- rebuilt

* Wed Jan 18 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.1-2
- moved translations to lxqt-l10n

* Sat Jan 07 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.1-1
- new version

* Mon Sep 26 2016 Helio Chissini de Castro <helio@kde.org> - 0.11.0-1
- New upstream version 0.11.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Helio Chissini de Castro <helio@kde.org> - 0.10.0-4
- Adapt for the new lxqt build that allows usage on epel as well (cmake3)

* Thu Jan 14 2016 Raphael Groner <projects.rg@smart.ms> - 0.10.0-3
- add BR: cmake, needed explicitly for epel7

* Sat Jan 09 2016 Raphael Groner <projects.rg@smart.ms> - 0.10.0-2
- own translations folder

* Sun Dec 20 2015 Raphael Groner <projects.rg@smart.ms> - 0.10.0-1
- initial
