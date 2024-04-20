# Retrofitting Principles

## Retrofitting and renovation
**TODO**  
The process of building energy retrofitting involves enhancing the energy efficiency and sustainability of existing structures by upgrading systems and features, integrating technology, materials, and practices to minimize energy consumption and reduce greenhouse gas emissions.

## Step by step retrofitting

![Retrofitting components step by step [@Passipedia2019] \label{fig:RetrofitComponents}](figs/retrofittingComponents.png){width=80%}

Step-by-step retrofitting is a process of improving the energy efficiency of a building through a series of planned renovations over time. This approach is particularly useful for buildings that were constructed before energy efficiency standards were widely adopted. The step-by-step retrofitting process has direct implications on the improvement of building stocks’ energy efficiency, and consequently, the achievement of decarbonisation targets set for 2050.(I. Maia et al., 2021)
Staged renovations are the most common across Europe, with 85% of renovations in Germany being staged. This approach allows for less disruptive and more cost-efficient renovation measures by aligning them with given ‘trigger points’. [@Fritz2019] Trigger points are circumstances that initiate home improvement projects unrelated to energy savings, providing an opportunity to modernize the energy performance of houses. There are two methods for retrofitting a house: the single-step method, where all measures are implemented simultaneously, and a phased approach, including room-by-room, measure-by-measure, and step-by-step sub-categories. The step-by-step retrofitting strategy highlights the adaptability of building energy retrofitting to align with stakeholders' cost constraints. 
The step-by-step retrofitting process is a strategic approach to building renovation that considers the timing, cost, and interdependencies of various renovation measures. It aims to maximize energy savings and contribute to the decarbonisation of the building sector[@Maia2021].

## Source-Code

```{.python caption="The preprocessing step, cf. [@Dietz2018]" #lst:huh}
def foo():
  """ Wuppie! """
  pass
```

## Mathe

Display-Math geht wie in \LaTeX{} mit einem doppelten Dollarzeichen (entspricht der `equation`-Umgebung):

$$
    \label{eq:wuppie}
    \nabla E(\mathbf{w}) = \left( \frac{\partial E}{\partial w_{0}}, \frac{\partial E}{\partial w_{1}}, \ldots, \frac{\partial E}{\partial w_{n}} \right)^T
$$

Inline-Math geht mit einem einfachen Dollar-Zeichen: $\mathbf{w} \gets \mathbf{w} + \Delta\mathbf{w}$ ...


## Tabellen

| Rechtsbündig | Linksbündig | Default | Zentriert |
|-------------:|:------------|---------|:---------:|
|          foo | foo         | foo     |    foo    |
|          123 | 123         | 123     |    123    |
|          bar | bar         | bar     |    bar    |

: Tabelle als Markdown-Pipe-Table, vgl. [@Dietz2018] \label{tab:ugh}


Leider gibt es derzeit einen Bug (siehe [github.com/Wandmalfarbe/pandoc-latex-template/issues/29](https://github.com/Wandmalfarbe/pandoc-latex-template/issues/29)
bzw. [github.com/jgm/pandoc/issues/3929](https://github.com/jgm/pandoc/issues/3929)), wodurch die Breite beim Einfärben der
Tabellenzeilen etwas zu breit wird. Wenn das stört, kann man immer noch normale \LaTeX{}-Tabellen nutzen (siehe
Tabelle \ref{tab:ieks}).

\begin{longtable}[]{rllc}
\caption{Tabelle als \LaTeX{}-Table \label{tab:ieks}} \\
\toprule
Rechtsbündig & Linksbündig & Default & Zentriert \tabularnewline
\midrule
\endhead
foo & foo & foo & foo \tabularnewline
123 & 123 & 123 & 123 \tabularnewline
bar & bar & bar & bar \tabularnewline
\bottomrule
\end{longtable}


## Querverweise

Querverweise funktionieren in Markdown leider nicht so richtig wie von \LaTeX{} gewohnt.

Hier kann aber einfach auf die ensprechenden \LaTeX{}-Pendants ausgewichen werden:

*   Definieren einer Referenz mit `\label{<id>}`{.latex} (beispielsweise in den jeweiligen Unterschriften
    unter einer Abbildung/Tabelle/Code-Schnipsel), und
*   Bezugnahme auf eine Referenz im Text mit `\ref{<id>}`{.latex}.

Vgl. Abbildung \ref{fig:foo} oder Tabelle \ref{tab:ugh} oder Listing \ref{lst:huh} ...

Wer mehr braucht, kann sogenannte Filter^[vgl. [pandoc.org/filters.html](https://pandoc.org/filters.html)
bzw. [pandoc.org/lua-filters.html](https://pandoc.org/lua-filters.html)] einsetzen, beispielsweise
[github.com/lierdakil/pandoc-crossref](https://github.com/lierdakil/pandoc-crossref).


## Hinweise zum generierten PDF

Das generierte PDF ist für den **doppelseitigen** Ausdruck gedacht. Wie bei einem Buch fangen neue Kapitel
immer auf einer neuen rechten Seite an, d.h. es kann passieren, dass am Ende eines Kapitels ggf. eine leere
Seite erzeugt wird. Dies ist durchaus beabsichtigt.
