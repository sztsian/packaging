%global project skilion
%global repo onedrive

Name:           onedrive
Version:        1.0.1
Release:        1%{?dist}
Summary:        OneDrive Free Client written in D
License:        GPLv3
URL:            https://github.com/%{project}/%{repo}
Source0:        %{url}/archive/v%{version}/%{repo}-v%{version}.tar.gz
BuildRequires:  ldc
BuildRequires:  libcurl-devel
BuildRequires:  sqlite-devel
BuildRequires:  systemd
Requires(post): systemd
Requires(preun): systemd 
ExclusiveArch:  %{ldc_arches}

%description
Free CLI client for Microsoft OneDrive written in D.
OneDrive for business is not supported.

%prep
%setup -q -n %repo-%{version}
sed -i 's|dmd|ldmd2|g' Makefile
sed -i 's|version||g' Makefile
sed -i '/git/d' Makefile
sed -i "s|/usr/local|%_prefix|" Makefile
echo %{version} >version
%build
export DFLAGS="%{_d_optflags}"
%make_build

%install
%make_install \
    PREFIX="%{_prefix}"

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%check
make unittest

%files
%doc README.md config
%license LICENSE
%{_bindir}/%{name}
%{_userunitdir}/%{name}.service

%changelog
* Thu Nov 30 2017 Zamir SUN <sztsian@gmail.com> 1.0.1-1
- Update to upstream release version 1.0.1

* Tue Oct 25 2016 mosquito <sensor.wen@gmail.com> 0.1.1-2.giteb8d0fe
- add BReq systemd

* Thu Oct 20 2016 Zamir SUN <sztsian@gmail.com> 0.1.1-1.giteb8d0fe
- initial package
