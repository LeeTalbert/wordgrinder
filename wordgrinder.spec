%global debug_package %{nil}

Name:		wordgrinder
Version:	0.9.dev
Release:	1
Source0:	https://github.com/davidgiven/wordgrinder/archive/refs/tags/dev.tar.gz#/%{name}-%{version}.tar.gz
Patch0:     wordgrinder-install.patch
Summary:	WordGrinder is a simple, Unicode-aware word processor that runs on the console.
URL:		https://github.com/davidgiven/wordgrinder
License:	MIT
# Some of the included bits use MIT, BSD, Open Font License, SCOWL copyright.
Group:		Terminal/Editors

BuildRequires:	ninja
BuildRequires:	lib64z-devel
BuildRequires:	lib64glfw-devel
BuildRequires:  pkgconfig(opengl)
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	python%{pyver}dist(pypillowfight)

Requires:	lib64ncursesw
Requires:	lib64z1
Requires:	lib64glfw3

%description
WordGrinder is a simple, Unicode-aware word processor that runs on the
console. It's designed to get the hell out of your way and let you write;
it does very little, but what it does it does well.

It supports basic paragraph styles, basic character styles, basic screen
markup, a menu interface that means you don't have to remember complex
key sequences, HTML import and export, and some other useful features.

%prep
%autosetup -p1 -n %{name}-dev -N
%autopatch -p0

%build
%make_build

%install
rm -rf %{buildroot}
%make_install PREFIX=%{_prefix} DESTDIR=%{buildroot}

%files
%doc licenses/*
%{_bindir}/%{name}
%{_bindir}/x%{name}
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/x%{name}.1*
