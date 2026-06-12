#! python
# %% import
import rivtlib.rvapi as rv


# The following settings change defaults (shown n parenthesis) for each doc.
# A leading hash (#) and trailing semicolon (;) are required.
# rv set_width = 80  ; character width of text output (80)
# rv no_tag = true ; if false, the API type is added to section number (true)
# rv private = true ; if false, default section heading changed to public (private)


# %% project description
rv.I("""Project description
     
    Design of embedded pole foundation for the flagpole design example in
    Appendix A of NAAMM/FP 1001-07, "Guide Specifications for Design of Metal
    Flagpoles" Embedded pole foundation design is per 2024 IBC Eq 6-1 and Table
    18-I-A. Soil properites are per Table 1806.2 in the 2024 IBC.

""")

# %% design input
rv.V("""Design input 
     

    | IMAGE | rvsrc/image1.png | Calculation Diagram, 25, num, not  

    Design input _[T]
    Mbase ==: 24.835 * ftkips |ftkips, mkN, 2 | moment at base of flagpole
    P ==: 24.835 * kips |kips,kN,2| horizontal load
    b ==: 24 * inch |inch, cm, 2 | width of concrete drilled pier
    PFP ==: 200 * pcf | pcf, kN_m3, 2| allowable lateral bearing pressure - sandy gravel  
    h ==: 1.5 * ft | ft, m, 2| height
    d ==: 10 * ft | ft, m, 2| initial guess for embedment depth   


    This command loads Python functions from a file.

    | PYTHON | rvsrc/pole_embed.py | Iterative functions

    """)

# %%
rv.V("""Design Results 
  
    depth_1 :=: Depth_nonconstrained (d, P, h, b, PFP, 2) | ft, m, 2 | Required embed - nonconstrained
     
    depth_2 :=: Depth_constrained (d, P, h, b, PFP) | ft, m, 2 | Required embed - constrained

    """)

# %% publish doc
rv.D("""Publish doc

    | PUBLISH | Flag Pole Foundation | txt

    _[[METADATA]] 
    [doc]
    authors = R Ward
    version = 1.0.0a12
    repo = -
    license = https://opensource.org/license/mit/
    copyright = -
    fork1_authors = -
    fork1_version = -
    fork1_repo = -
    fork1_license = https://opensource.org/license/mit/

    [layout]
    title = Flag Pole Embedment
    subtitle =  Example 2 - rivt Doc  
    copyright = --
    client = User Example
    coverpage = true
    coverlogo = logo2.png
    coverlogo_size = 50
    runninglogo = rwlogo.png
    runninglabel = Robert Ward SE
    project_ref = proj. 0002
    pdf_pagesize = letter
    pdf_margins = 1in, 1in, 1in, 1in 
    pdf_link_underline = false
    ;----- table of contents levels: = 1 shows subdivisions, = 2 includes sections. 
    toc_level = 2

    [process]
    doc_verbose = true; if false, minimum output during doc processing
    auto_cfg = true ; if false, config files are not updated from rivt file
    _[[END]]
    

""")
