%global octpkg fpl

Summary:	Octave support for various graphical formats
Name:		octave-fpl
Version:	1.3.5
Release:	2
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/fpl/
Source0:	https://downloads.sourceforge.net/octave/fpl-%{version}.tar.gz

BuildRequires:  octave-devel >= 3.2.3

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

BuildArch:	noarch

%description
Collection of routines to export data produced by Finite Elements or
Finite Volume Simulations in formats used by some visualization
programs.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}

%build
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

