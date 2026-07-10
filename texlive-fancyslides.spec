%global tl_name fancyslides
%global tl_revision 36263

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Custom presentation class built upon LaTeX Beamer
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fancyslides
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fancyslides.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fancyslides.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This class is prepared for short presentations with a modern look &
feel. It offers the following features: custom background for each
slide, predefined types of slides, simplified commands (e.g. for
starting and ending slide). The class is built upon LaTeX beamer, so all
beamer commands should work.

