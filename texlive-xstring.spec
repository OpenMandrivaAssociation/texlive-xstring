%global tl_name xstring
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.86
Release:	%{tl_revision}.1
Summary:	String manipulation for (La)TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/xstring
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xstring.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xstring.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides macros for manipulating strings -- testing a
string's contents, extracting substrings, substitution of substrings and
providing numbers such as string length, position of, or number of
recurrences of, a substring. The package works equally in Plain TeX and
LaTeX (though e-TeX is always required). The strings to be processed may
contain (expandable) macros.

