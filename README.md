# Exploration of LLM Reliability

<div align="center">


  <h3 align="center">LLM Format Adherence Analysis</h3>

  <p align="center">
    An exploration of LLM reliability and consistency in structured output generation
    <br />
    <a href="#about-the-project">About The Project</a>
    ·
    <a href="#methodology">Methodology</a>
    ·
    <a href="https://www.linkedin.com/in/ryjocochran/">Who Am I?</a> <!--eventually this should link to my resume -->
  </p>
</div>

<div align="center">
  
[![LLM Testing Results][funnyjpg]](https://xkcd.com/1838/)

</div>

## About The Project

### This is a living document!

As I dive deeper into this area of research I will update this document to explain the tests being conducted as well as include any additional resources I find in this section. I am in the fortunate position of being a development resource to my friends and coworkers, I intend for this section to be a quick way to dive into the best work on this topic. 
#### Reading for Nerds
* [Chroma Context Rot Research](https://research.trychroma.com/context-rot)
* [(Interesting BTS interview of the Chroma Research ^)](https://youtu.be/PGMtF5PHeDI)
* [Gao, Xiong, Wu, Huang, Li, Wang, 2025](https://arxiv.org/abs/2503.00353)
* [Khatun, 2024 (Ch7 Specifically)](https://uwspace.uwaterloo.ca/items/e01e11a6-e033-4f6a-85c6-849fba74e039)
* [Lee, Hong, Thorne, 2024](https://arxiv.org/abs/2412.00543)
* [Patwardhen, Vaidya, Kundu, 2025](https://arxiv.org/abs/2502.07036)
#### Datasets/Libraries
* [Berka Dataset Documentation](https://webpages.charlotte.edu/mirsad/itcs6265/group1/domain.html)
* [Northwind Database Reference](https://docs.yugabyte.com/preview/sample-data/northwind/)
* [Ollama Project](https://github.com/ollama/ollama)
* [Pandas Documentation](https://pandas.pydata.org/)

### Outline

This project investigates a fundamental question in Large Language Model (LLM) deployment: **Can LLMs maintain consistent adherence to formatting rules even when faced with noisy or unrelated queries?**

This exploration examines the reliability of instruction-following versus structured output approaches, particularly testing whether LLMs can maintain designated response formats when queries fall outside their intended domain. The work was prompted from reading [context rot](https://research.trychroma.com/context-rot) and explores practical implications for production LLM systems.

### Motivation 
The rapid evolution of LLM capabilities has created both opportunities and challenges in production environments. While these models demonstrate remarkable flexibility, questions remain about their reliability in structured, predictable workflows - particularly when handling edge cases or unexpected inputs. This exploration originated as a component of a larger database analysis product I am developing, and while I don't typically use GitHub as my primary version control solution, I wanted to share this work publicly to demonstrate my process of technical exploration and development to peers and potential collaborators, while also contributing to the broader understanding of LLM deployment challenges in production systems.

### Key Questions Explored

* How consistently do different LLMs follow formatting instructions across varied input types?
* Is forcing structured output from LLMs (via Pydantic) papering over a fundamental failure?
* How do context vectors perform under stress testing with random, human-like queries?

### Project Context

This exploration is part of a larger database schema analysis project, where LLMs are tested on their ability to:
- Parse SQL Server information schemas
- Identify relevant tables for user queries
- Maintain consistent output formats across diverse inputs

Test datasets include:
- **Berka Dataset**: Well-behaved test case for LLM parsing
- **Northwind Database**: Standard reference implementation
- **Random Generated Dataset**: Stressed data engineering test case with realistic SQL server conditions

Built With

* [![Python][Python.py]][Python-url]
* [![Ollama][Ollama.ai]][Ollama-url]
* [![Pandas][Pandas.py]][Pandas-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Methodology

### Testing Approach

1. **Baseline Testing**: Simple, clear instructions with expected outputs
2. **Stress Testing**: Random queries unrelated to the intended task
3. **Format Consistency**: Measuring adherence to output specifications
4. **Cross-Model Comparison**: Evaluating different model architectures

### Data Collection

The project systematically collects:
- Response consistency across iterations
- Timing performance data
- Format adherence metrics
- Error rates and failure modes

### Possible Future Enhancements

- [ ] Integration with Reddit API / Lorem generator for random human-like query generation
- [ ] Pydantic structured output comparison
- [ ] Schema analysis workflow implementation
- [ ] Automated consistency scoring
- [ ] Statistical significance testing

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Key Concepts
This exploration addresses critical questions for production LLM systems:

**Context Vector Reliability**: If LLMs cannot maintain basic formatting consistency, what does this mean for context window utilization and prompt engineering strategies?

**Production Readiness**: Understanding when to rely on LLM interpretation versus traditional fuzzy matching and parsing approaches.

**Cost-Benefit Analysis**: Evaluating the overhead of structured output layers versus instruction-based approaches.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[funnyjpg]: docs/machine_learning.png
[Python.py]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://python.org/
[Ollama.ai]: https://img.shields.io/badge/Ollama-000000?style=for-the-badge&logo=ollama&logoColor=white
[Ollama-url]: https://ollama.ai/
[Pandas.py]: https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white
[Pandas-url]: https://pandas.pydata.org/