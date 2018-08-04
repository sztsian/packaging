Name:    lxqt-admin
Summary: LXQt system administration tool
Version: 0.13.0
Release: 1%{?dist}
License: LGPLv2+
URL:     http://lxqt.org/
Source0: https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:  https://github.com/lxde/%{name}/commit/15779a479e7659387105c57e993b7a350bd94400.patch
BuildRequires:  pkgconfig(lxqt)
BuildRequires:  desktop-file-utils
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  lxqt-build-tools
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  qt5-linguist
BuildRequires:  pkgconfig(polkit-qt5-1)
Requires:       polkit

%description
This package provides tools to adjust settings of the operating system
LXQt is running on. Both can be launched from GUI "Configuration Center".

GUI "Time and date configuration", binary lxqt-admin-time, can be used
to adjust the system time of the operating system as well as the timezone.

%prep
%autosetup -p1 

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
   %{cmake_lxqt} -DUSE_QT5=TRUE -DPULL_TRANSLATIONS=NO ..
popd
make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

for admfile in user time; do
desktop-file-edit \
    --remove-category=LXQt --add-category=X-LXQt \
    --remove-category=Help --add-category=X-Help \
    --remove-only-show-in=LXQt --add-only-show-in=X-LXQt \
    %{buildroot}%{_datadir}/applications/%{name}-${admfile}.desktop
done


%files 
%license COPYING
%doc AUTHORS README.md
%{_bindir}/%{name}*
%{_datadir}/applications/%{name}*.desktop
%{_datadir}/polkit-1/actions/*.policy

%changelog
* Fri Aug 03 2018 Zamir SUN <zsun@fedoraproject.org> - 0.13.0-1
- Update to version 0.13.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 10 2017 Raphael Groner <projects.rg@smart.ms> - 0.11.1-5
- add upstram patch to avoid duplicates, rhbz#1459642

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 19 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.1-3
- rebuilt

* Wed Jan 18 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.1-2
- moved translations to lxqt-l10n

* Sat Jan 07 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.1-1
- new version

* Sun Sep 25 2016 Helio Chissini de Castro <helio@kde.org> - 0.11.0-1
- New upstream version 0.11.0

* Sat Aug 06 2016 Raphael Groner <projects.rg@smart.ms> - 0.10.0-3.20160729git2f95601
- new git snapshot
- fix unlicensed files

* Wed Jul 06 2016 Raphael Groner <projects.rg@smart.ms> - 0.10.0-2.20160705git8acfd2a
- new git snapshot
- drop dependency to liboobs
- add polkit
- adjust license

* Tue Jun 07 2016 Raphael Groner <projects.rg@smart.ms> - 0.10.0-1.20160531git0f9ab3a
- initial
