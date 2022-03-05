%define octpkg fpl

Summary:	Octave support for various graphical formats
Name:		octave-%{octpkg}
Version:	1.3.5
Release:	1
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/
BuildArch:	noarch

BuildRequires:	octave-devel >= 3.2.3

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
Collection of Octave routines to export data produced by Finite Elements or
Finite Volume Simulations in formats used by some visualization programs.

This package is part of external Octave-Forge collection.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -n %{octpkg}

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

