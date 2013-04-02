Name:           gnu-efi
Version:        3.0
Release:        1
License:        BSD-3-Clause
Summary:        EFI development environment
Url:            http://sourceforge.net/projects/gnu-efi/
Group:          System/Boot
Source0:        http://download.sourceforge.net/%{name}/%{name}_%{version}.orig.tar.gz
BuildRequires:  pciutils


%description
gnu-efi is a library for building EFI applications

%prep
%setup -q -n %{name}-%{version}

%build
make

%install
make install PREFIX=%{_prefix} INSTALLROOT=%{buildroot}

%files
%defattr(-,root,root)
%{_includedir}/efi/*
%{_prefix}/lib/*
