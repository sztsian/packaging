%global commit 2ef3f812335d216a9aaf72e8473dc51dfd3a453e
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           kabi-dw
Version:        0
Release:        0.1.20171012git%{shortcommit}%{?dist}
Summary:        Detect changes in the ABI between kernel builds
License:        GPLv3+
URL:            https://github.com/skozina/%{name}
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  elfutils-devel
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libasan
BuildRequires:  glib2-devel

%description
The aim of kabi-dw is to detect any changes in the ABI between the successive builds of the Linux kernel. This is done by dumping the DWARF type information (the .debug_info section) for the specific symbols into the text files and later comparing the text files.

%prep
%setup -q -n %{name}-%{commit}

%build
%make_build debug

%install
install -dm 755 %{buildroot}%{_bindir}
install -m 0755 %{name} %{buildroot}%{_bindir}/

%files
%{_bindir}/%{name}
%doc README.md
%license COPYING

%changelog
* Mon Oct 16 2017 Zamir SUN <zsun@fedoraproject.org> - 0-0.1.20171012git2ef3f81
- Initial package kabi-dw
