%global debug_package %{nil}

Name:		yazi
Version:	25.4.8
Release:	1
Source0:	https://github.com/sxyazi/yazi/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}-%{version}-vendor.tar.gz
Summary:	Blazing fast terminal file manager written in Rust, based on async I/O.
URL:		https://github.com/sxyazi/yazi
License:	MIT
Group:		Application/File Manager

BuildRequires:	cargo

%description
Yazi (means "duck") is a terminal file manager written in Rust, based on non-blocking async I/O. It aims to provide an efficient, user-friendly, and customizable file management experience.

%prep
%autosetup -p1
tar -zxf %{SOURCE1}
mkdir -p .cargo
cat >> .cargo/config.toml << EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

EOF

%build
cargo build --frozen --release

%install
install -Dpm 0755 -t %{buildroot}%{_bindir} target/release/yazi target/release/ya

%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE
%license LICENSE-ICONS
%doc README.md
%{_bindir}/ya
%{_bindir}/yazi
