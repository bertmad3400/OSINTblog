title: About The Project
date: 2022-07-03
author: Bertmad
description: A short description of OSINTer as a project

## The Project
### What problem does OSINTer attempt to solve?

The process of gathering cyber threat intelligence is only as successful as the investigators ability to identify relevant intelligence sources. Identifying relevant and reliable sources could often be a time-consuming task, as the CTI personnel would have to first locate the intelligence source, then read it to identify its relevance and usefulness as well as identify its formatting, and finally mark down all relevant details for usage in their report. This is time consuming and can be hit and miss depending on the skill and experience of the CTI personnel, and while products to combat this repetitive and time-consuming task, like Recorded Future, exists, these are often not only expensive, but also closed in nature, as they rarely integrate well with thirdparty utilities.

The goal of OSINTer is to build an open-source and extensible platform for collecting and organizing open-source intelligence in a way that easily intergrates with thirdparty utilities and other pieces of open-source software. As such, it never was (and never will be) intended to compete with products like the aforementioned Recorded Future, since the core concept is very different and since OSINTer does not offer the needed analysis capabilities on its own.

### How does OSINTer Solve the Problem?

Firstly, to combat the time-consuming task of identifying relevant threat intelligence sources, OSINTer gathers information from known, reliable sources, automatically, and then displays these in its webservice interface in a list sorted by publish date. This provides the most current information first, and in a consistent format so that users can easily identify the relevant information sources for their CTI reports or other use cases.

Secondly, the content from the threat intelligence sources is archived and retrievable for the user, through a download functionality in OSINTer, which allows for download Markdown files containing this content, and formattet in a consisten fashion. These files, when imported into any markdown editor (preferably Obsidian), allows the user to analyze on all or parts of the collected information. Obsidian has tools to easily detect correlations between the information, providing a much-needed overview of the collected information.
How do we intend to use OSINTer?

Our current intent with OSINTer is deploying it internally where needed as to aid CTI team in easily identify relevant sources for future CTI reports, and to deploy a single central instance of OSINTer to start building an archive of historical data.
