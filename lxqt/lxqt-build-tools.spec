Name:           lxqt-build-tools
Version:        0.5.0
Release:        1%{?dist}
Summary:        Packaging tools for LXQt

License:        BSD
URL:            http://lxqt.org/
Source0:        https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  %{?fedora:cmake}%{!?fedora:cmake3} >= 3.0
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(glib-2.0)

Requires:       %{?fedora:cmake}%{!?fedora:cmake3} >= 3.0

%description
Various packaging tools and scripts for LXQt applications.


%prep
%autosetup -p1
%{__mkdir} -p %{_target_platform}


%build
pushd %{_target_platform}
%{?fedora:%{cmake}}%{!?fedora:%{cmake3}} ..
popd
%make_build -C %{_target_platform}


%install
%make_install -C %{_target_platform}


%files
%license BSD-3-Clause
%doc CHANGELOG README.md
%{_datadir}/cmake/%{name}


%changelog
* Fri Aug 03 2018 Zamir SUN <zsun@fedoraproject.org> - 0.5.0-1
- Update to 0.5.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 15 2017 Christian Dersch <lupinix@mailbox.org> - 0.3.2-1
- new version (0.3.2)
- patch to make package noarch'ed removed, has been upstreamed

* Fri Jan 06 2017 Björn Esser <besser82@fedoraproject.org> - 0.3.1-3
- Build out-of-tree

* Fri Jan 06 2017 Björn Esser <besser82@fedoraproject.org> - 0.3.1-2
- Update Patch0 to make the whole package noarch'ed
- Add `BuildArch: noarch`
- Clean trailing whitespaces

* Mon Jan  2 2017 Christian Dersch <lupinix@mailbox.org> - 0.3.1-1
- initial package
