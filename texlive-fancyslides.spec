Name:		texlive-fancyslides
Version:	36263
Release:	1
Summary:	Custom presentation class built upon LaTeX Beamer
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fancyslides
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancyslides.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancyslides.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This class is prepared for short presentations with a modern
look & feel. It offers the following features: custom
background for each slide, predefined types of slides,
simplified commands (e.g. for starting and ending slide). The
class is built upon LaTeX beamer, so all beamer commands should
work.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/fancyslides
%doc %{_texmfdistdir}/doc/latex/fancyslides

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
