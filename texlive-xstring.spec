# revision 31305
# category Package
# catalog-ctan /macros/generic/xstring
# catalog-date 2013-07-29 13:50:09 +0200
# catalog-license lppl
# catalog-version 1.7b
Name:		texlive-xstring
Version:	1.7b
Release:	1
Summary:	String manipulation for (La)TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/xstring
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xstring.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xstring.doc.tar.xz
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
%{_texmfdistdir}/tex/generic/xstring/xstring.sty
%{_texmfdistdir}/tex/generic/xstring/xstring.tex
%doc %{_texmfdistdir}/doc/generic/xstring/README
%doc %{_texmfdistdir}/doc/generic/xstring/xstring_doc_en.pdf
%doc %{_texmfdistdir}/doc/generic/xstring/xstring_doc_en.tex
%doc %{_texmfdistdir}/doc/generic/xstring/xstring_doc_fr.pdf
%doc %{_texmfdistdir}/doc/generic/xstring/xstring_doc_fr.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
