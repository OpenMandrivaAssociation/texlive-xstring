Name:		texlive-xstring
Version:	60007
Release:	2
Summary:	String manipulation for (La)TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/xstring
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xstring.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xstring.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides macros for manipulating strings -- testing
a string's contents, extracting substrings, substitution of
substrings and providing numbers such as string length,
position of, or number of recurrences of, a substring. The
package works equally in Plain TeX and LaTeX (though e-TeX is
always required). The strings to be processed may contain
(expandable) macros.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/xstring
%doc %{_texmfdistdir}/doc/generic/xstring

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
