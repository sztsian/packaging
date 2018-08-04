Name:           lxqt-themes-fedora
Version:        1.0
Release:        0.1%{?dist}
Summary:        Fedora LXQt themes

License:        LGPLv2+ and CC-BY-SA
URL:            https://pagure.io/lxqt-themes-fedora
Source0:        %{name}-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  lxqt-build-tools
BuildRequires:  pkgconfig(lxqt)

Requires:       lxqt-themes

# Obsolete and provide the old subpackage of lxqt-common
Provides:       lxqt-theme-fedora = %{version}-%{release}
Obsoletes:      lxqt-theme-fedora < %{version}-%{release}

%description
This package contains Fedora themes for the LXQt desktop environment.

%package sddm
Summary:        Fedora LXQt theme for SDDM
License:        CC-BY-SA
Requires:       sddm

%description sddm
This package contains the SDDM theme for Fedora LXQt.

%prep
%autosetup


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
    %{cmake_lxqt} ..
popd
%make_build -C %{_target_platform}

%install
make install DESTDIR=%{buildroot} -C %{_target_platform}

%files
%license lxqt/COPYING
%{_datadir}/lxqt/themes/fedora-lxqt

%files sddm
%license sddm/02-lxqt-fedora/LICENSE
%{_datadir}/sddm/themes/02-lxqt-fedora

%changelog
* Sun Jun 10 2018 Christian Dersch <lupinix@mailbox.org> - 1.0-0.1
- initial package
