#! python
import rivtlib.rvapi as rv


# The following settings change defaults (shown n parenthesis) for each doc. xx
# A leading hash (#) and trailing semicolon (;) are required.
# rv set_width = 80  ; character width of text output (80)
# rv no_tag = true ; if false, the API type is added to section number (true)
# rv private = true ; if false, default section heading changed to public (private)



# %% rv.I("""Project description
rv.I("""Project description
     
    Design of embedded pole foundation for the flagpole design example in
    Appendix A of NAAMM/FP 1001-07, "Guide Specifications for Design of Metal
    Flagpoles" Embedded pole foundation design is per 2024 IBC Eq 6-1 and Table
    18-I-A. Soil properites are per Table 1806.2 in the 2024 IBC.
    
    """)

# %% rv.V("""Design input 
rv.V("""Design input 
     
    | IMAGE | rvsrc/img/image1.png | Calculation Diagram, 25, num, not  

    Design input _[T]
    Mbase ==: 24.835 * ftkips |ftkips, mkN, 2 | moment at base of flagpole
    P ==: 24.835 * kips |kips,kN,2| horizontal load
    b ==: 24 * inch |inch, cm, 2 | width of concrete drilled pier
    PFP ==: 200 * p_cf | p_cf, kN_m3, 2| allowable lateral bearing pressure - sandy gravel  
    h ==: 1.5 * ft | ft, m, 2| height
    d ==: 10 * ft | ft, m, 2| initial guess for embedment depth   

    ## This command loads Python functions from a file.

    | PYTHON | rvsrc/scripts/pole_embed.py | Iterative functions
    
    """)

# %% rv.V("""Design Results 
rv.V("""Design Results 
  
    depth_1 :=: Depth_nonconstrained (d, P, h, b, PFP, 2) | ft, m, 2 | Required embed - nonconstrained
     
    depth_2 :=: Depth_constrained (d, P, h, b, PFP) | ft, m, 2 | Required embed - constrained
    
    """)
# %% rv.D("""Publish doc
rv.D("""Publish doc

    | PUBLISH | Example 2 - Flagpole Foundation | txt

    _[[METADATA]] 
    [process]
    ;-----------------------------------------
    doc_verbose = true; if false minmize output during doc processing
    auto_cfg = true ; if false, config files are not updated from rivt file
    [doc]
    ;-----------------------------------------
    authors = R Holland
    version = 1.0.0a13
    repo = https://github.com/rivt-info/rivt-single-doc
    license = https://opensource.org/license/mit/
    copyright = --
    fork1_authors = --
    fork1_version = --
    fork1_repo = --
    fork1_license = https://opensource.org/license/mit/
    [layout]
    ;----------------------- cover page and runner settings
    ;--- add logo files to rvsrc/img folder, size is % page width
    subtitle =  Pole Embedment
    copyright = --
    client = user example
    coverpage = true
    coverlogo = rwlogo.png
    coverlogo_size = 50
    runninglogo = rwlogo.png
    runninglabel = Robert Ward SE
    project_ref = proj. 0003
    ;------------------------ PDF settings
    ;--- colors: red, blue, green, black, gray, brown, maroon, gray, olive, cyan
    ;--- margins: top, right, bottom, left    page size: letter, legal, A4    
    pdf_link_color = black
    pdf_link_underline = true
    pdf_pagesize = letter
    pdf_margins = 1in, 1in, 1in, 1in 
    ;----------------------- TOC levels
    ;--- 1: include subdivisions   2: include subdivisions and sections
    toc_level = 2
    _[[END]]
    """)
