// Auto-generated data bundle for GitHub Pages
const METHODS_DATA = [
  {
    "id": "survey",
    "name": "Survey Research",
    "category": "quantitative",
    "status": "draft - needs faculty verification",
    "description": "A structured quantitative method used to systematically gather numerical data from a predefined sample of respondents to describe, compare, or explain characteristics, attitudes, opinions, or behaviors.",
    "best_used_when": "When researchers aim to generalize findings from a representative sample to a larger population, describe prevailing attitudes, or test statistical relationships across demographic segments.",
    "strengths": [
      "High generalizability when using representative probability sampling",
      "Cost-effective and time-efficient for large, geographically dispersed samples",
      "Facilitates standardized, reproducible statistical comparisons",
      "Minimizes interviewer bias through standardized questionnaire instruments"
    ],
    "limitations": [
      "Risk of non-response bias and low response rates",
      "Superficial data depth compared to open qualitative inquiries",
      "Susceptible to social desirability and self-reporting bias",
      "Inflexible once deployed; questions cannot be modified mid-study"
    ],
    "typical_data_collection": [
      "Online digital questionnaires (Qualtrics, Google Forms)",
      "Self-administered paper questionnaires",
      "Structured telephone or face-to-face interviews"
    ],
    "typical_analysis_techniques": [
      "Descriptive statistics (mean, median, standard deviation)",
      "Inferential tests (t-tests, ANOVA, Chi-Square)",
      "Regression modeling and factor analysis"
    ],
    "sample_size_guidance": "Typically 100+ respondents for statistical power; power analysis recommended for regression/factor analysis.",
    "time_required": "med",
    "cost": "low",
    "ethical_considerations": "Informed consent, voluntary participation, guarantee of respondent anonymity/confidentiality, and secure data storage.",
    "example_use_cases": [
      {
        "domain": "education",
        "title": "Undergraduate Perceptions of AI Tutoring Tools",
        "scenario": "Administering a validated 5-point Likert questionnaire to 350 university students to evaluate their satisfaction, usability perceptions, and perceived academic benefits."
      },
      {
        "domain": "management",
        "title": "Employee Hybrid-Work Satisfaction & Turnover Intention",
        "scenario": "Surveying 220 knowledge workers across IT firms to examine the statistical relationship between remote work flexibility and organizational commitment."
      }
    ],
    "suitable_domains": [
      "education",
      "management",
      "social science",
      "health"
    ],
    "references": [
      {
        "author": "Creswell, J. W., & Creswell, J. D.",
        "year": 2018,
        "title": "Research Design: Qualitative, Quantitative, and Mixed Methods Approaches (5th ed.)",
        "publisher_or_journal": "SAGE Publications"
      },
      {
        "author": "Kothari, C. R.",
        "year": 2004,
        "title": "Research Methodology: Methods and Techniques (2nd ed.)",
        "publisher_or_journal": "New Age International Publishers"
      }
    ]
  },
  {
    "id": "experiment",
    "name": "True Experimental Design",
    "category": "quantitative",
    "status": "draft - needs faculty verification",
    "description": "A rigorous quantitative design that isolates cause-and-effect relationships through deliberate manipulation of an independent variable, random assignment of participants into experimental and control groups, and strict experimental control over extraneous variables.",
    "best_used_when": "When the primary research objective is to test specific causal hypotheses with maximum internal validity under controlled settings.",
    "strengths": [
      "Gold standard for demonstrating unambiguous causality (cause-and-effect)",
      "High internal validity through random assignment and control groups",
      "High reproducibility and standardization across laboratory environments"
    ],
    "limitations": [
      "Potential artificiality; findings may not easily translate to naturalistic environments (lower ecological validity)",
      "Strict ethical constraints regarding interventions that could harm participants",
      "Resource-intensive in laboratory setup, specialized instrumentation, and participant tracking"
    ],
    "typical_data_collection": [
      "Direct physiological or behavioral sensor measurements",
      "Standardized pre-test and post-test assessments",
      "Automated software logging (latency, error rates, completion time)"
    ],
    "typical_analysis_techniques": [
      "Independent-samples and paired t-tests",
      "Analysis of Variance (One-way and Factorial ANOVA)",
      "Analysis of Covariance (ANCOVA) for baseline adjustment"
    ],
    "sample_size_guidance": "30-100 participants partitioned across groups, determined via statistical power calculations (G*Power).",
    "time_required": "med",
    "cost": "med",
    "ethical_considerations": "Requires institutional review board (IRB) approval, strict risk mitigation, informed consent, and post-experiment participant debriefing.",
    "example_use_cases": [
      {
        "domain": "engineering",
        "title": "Code Review Speed Under Dark vs. Light IDE Themes",
        "scenario": "Randomly assigning 60 software developers to debug identical software modules using either dark or light theme to measure error identification latency."
      },
      {
        "domain": "health",
        "title": "Efficacy of a Digital Mindfulness App on Cortisol Levels",
        "scenario": "Randomized controlled trial (RCT) with 80 stressed adults divided into app-guided meditation vs. waitlist control group over 4 weeks."
      }
    ],
    "suitable_domains": [
      "engineering",
      "health",
      "education",
      "social science"
    ],
    "references": [
      {
        "author": "Campbell, D. T., & Stanley, J. C.",
        "year": 1963,
        "title": "Experimental and Quasi-Experimental Designs for Research",
        "publisher_or_journal": "Houghton Mifflin"
      },
      {
        "author": "Creswell, J. W., & Creswell, J. D.",
        "year": 2018,
        "title": "Research Design: Qualitative, Quantitative, and Mixed Methods Approaches",
        "publisher_or_journal": "SAGE Publications"
      }
    ]
  },
  {
    "id": "quasi_experiment",
    "name": "Quasi-Experimental Design",
    "category": "quantitative",
    "status": "draft - needs faculty verification",
    "description": "An empirical intervention study used to estimate the causal impact of an intervention on target populations without random assignment of participants, often using non-equivalent comparison groups or pre/post interrupted time-series.",
    "best_used_when": "When researchers test an intervention in real-world educational, clinical, or organizational settings where true random assignment is impractical or unethical.",
    "strengths": [
      "Higher ecological and practical validity than artificial laboratory experiments",
      "Feasible in authentic classroom, clinical, or workplace environments",
      "Provides valuable causal evidence when random assignment cannot be justified"
    ],
    "limitations": [
      "Lower internal validity than true experiments due to selection bias",
      "Potential confounding variables between non-equivalent control and treatment groups",
      "Requires sophisticated statistical controls (e.g., propensity score matching)"
    ],
    "typical_data_collection": [
      "Pre-test and post-test performance evaluations",
      "Organizational key performance indicators (KPIs)",
      "Attendance, clinical outcome, or learning metric archives"
    ],
    "typical_analysis_techniques": [
      "Difference-in-Differences (DiD) regression",
      "Repeated-measures ANOVA / ANCOVA",
      "Propensity Score Matching (PSM)"
    ],
    "sample_size_guidance": "30-100+ participants across intact cohorts or existing organizational units.",
    "time_required": "med",
    "cost": "med",
    "ethical_considerations": "Ensuring control cohorts are not unfairly deprived of beneficial educational or healthcare interventions (waitlist designs recommended).",
    "example_use_cases": [
      {
        "domain": "education",
        "title": "Impact of Flipped Classroom Pedagogy on Engineering Students",
        "scenario": "Comparing exam scores of Section A (flipped classroom) against Section B (traditional lecture) without randomly moving enrolled students."
      },
      {
        "domain": "management",
        "title": "Effectiveness of a New Agile Coaching Framework",
        "scenario": "Measuring sprint velocity differences across two regional development centers before and after deploying an agile coach to one center."
      }
    ],
    "suitable_domains": [
      "education",
      "management",
      "health",
      "social science"
    ],
    "references": [
      {
        "author": "Shadish, W. R., Cook, T. D., & Campbell, D. T.",
        "year": 2002,
        "title": "Experimental and Quasi-Experimental Designs for Generalized Causal Inference",
        "publisher_or_journal": "Wadsworth Cengage Learning"
      },
      {
        "author": "Kothari, C. R.",
        "year": 2004,
        "title": "Research Methodology: Methods and Techniques",
        "publisher_or_journal": "New Age International Publishers"
      }
    ]
  },
  {
    "id": "case_study",
    "name": "Case Study Research",
    "category": "qualitative",
    "status": "draft - needs faculty verification",
    "description": "An in-depth empirical inquiry that investigates a contemporary phenomenon within its real-life context, especially when the boundaries between phenomenon and context are not clearly evident, utilizing multiple sources of evidence.",
    "best_used_when": "When seeking to answer 'how' and 'why' questions about complex organizational, technological, or social events over which the investigator has little control.",
    "strengths": [
      "Rich, contextualized, deep qualitative insights",
      "Captures holistic and meaningful characteristics of real-life events",
      "Triangulates multiple evidentiary sources (interviews, documents, observations)"
    ],
    "limitations": [
      "Limited statistical generalizability beyond the examined case boundaries",
      "Potential researcher subjectivity in evidence interpretation",
      "Time-consuming data collection and complex cross-case synthesis"
    ],
    "typical_data_collection": [
      "In-depth semi-structured stakeholder interviews",
      "Archival records, internal policies, and email correspondence",
      "Field notes from direct on-site observations"
    ],
    "typical_analysis_techniques": [
      "Pattern matching and thematic analysis",
      "Cross-case synthesis (for multi-case designs)",
      "Process tracing and chronological explanation building"
    ],
    "sample_size_guidance": "1 to 5 bounded cases; within-case sampling of 10-30 qualitative informants.",
    "time_required": "high",
    "cost": "med",
    "ethical_considerations": "Protecting organizational proprietary confidentiality, anonymizing sensitive leadership decisions, and obtaining institutional consent.",
    "example_use_cases": [
      {
        "domain": "management",
        "title": "Cloud Migration Resistance in a Legacy Public Utility",
        "scenario": "Conducting a comprehensive 6-month single-case investigation of a public water utility transitioning its ERP system to the cloud."
      },
      {
        "domain": "engineering",
        "title": "Post-Mortem of a Safety-Critical Autonomous Vehicle Software Failure",
        "scenario": "Deep-dive case analysis of telemetry, engineering tickets, and developer communications leading up to an autonomous driving incident."
      }
    ],
    "suitable_domains": [
      "management",
      "engineering",
      "education",
      "social science"
    ],
    "references": [
      {
        "author": "Yin, R. K.",
        "year": 2018,
        "title": "Case Study Research and Applications: Design and Methods (6th ed.)",
        "publisher_or_journal": "SAGE Publications"
      },
      {
        "author": "Stake, R. E.",
        "year": 1995,
        "title": "The Art of Case Study Research",
        "publisher_or_journal": "SAGE Publications"
      }
    ]
  },
  {
    "id": "semi_structured_interview",
    "name": "Semi-Structured Interviews",
    "category": "qualitative",
    "status": "draft - needs faculty verification",
    "description": "A qualitative data collection and inquiry method guided by an overarching topical interview protocol with open-ended prompts, permitting the researcher flexibility to probe emergent thoughts, clarify meaning, and explore tangential insights.",
    "best_used_when": "When researchers require nuanced, individualized perspectives from key informants, subject matter experts, or participants about complex lived experiences or organizational decisions.",
    "strengths": [
      "Combines structural consistency with conversational exploratory flexibility",
      "Allows probing and real-time clarification of ambiguous answers",
      "Captures rich affective, personal, and context-specific narratives"
    ],
    "limitations": [
      "Transcription and coding of audio data is labor-intensive",
      "Susceptible to interviewer bias and leading questions",
      "Non-generalizable in a strict statistical sense"
    ],
    "typical_data_collection": [
      "Audio/video recorded one-on-one dialogue (in-person or Zoom/Teams)",
      "Interview guides with primary questions and probe questions",
      "Reflexive field notes and memos captured immediately post-interview"
    ],
    "typical_analysis_techniques": [
      "Thematic analysis (Braun & Clarke framework)",
      "Qualitative Content Analysis",
      "Inter-coder reliability verification (Cohen's Kappa)"
    ],
    "sample_size_guidance": "12 to 30 participants, continuing until theoretical or data saturation is achieved.",
    "time_required": "med",
    "cost": "low",
    "ethical_considerations": "Informed consent for audio recording, participant confidentiality, right to withdraw, and sensitive handling of personal disclosures.",
    "example_use_cases": [
      {
        "domain": "health",
        "title": "ICU Nurse Burnout During Surge Operations",
        "scenario": "Conducting 20 semi-structured interviews with senior critical-care nurses to understand coping mechanisms during prolonged emergency deployments."
      },
      {
        "domain": "engineering",
        "title": "DevSecOps Adoption Barriers in Financial Institutions",
        "scenario": "Interviewing 16 chief information security officers (CISOs) to explore friction between software delivery speed and security compliance."
      }
    ],
    "suitable_domains": [
      "health",
      "management",
      "education",
      "social science",
      "engineering"
    ],
    "references": [
      {
        "author": "Saunders, M., Lewis, P., & Thornhill, A.",
        "year": 2019,
        "title": "Research Methods for Business Students (8th ed.)",
        "publisher_or_journal": "Pearson Education"
      },
      {
        "author": "Kothari, C. R.",
        "year": 2004,
        "title": "Research Methodology: Methods and Techniques",
        "publisher_or_journal": "New Age International Publishers"
      }
    ]
  },
  {
    "id": "focus_group",
    "name": "Focus Group Discussions",
    "category": "qualitative",
    "status": "draft - needs faculty verification",
    "description": "A moderated group interview method where a selected group of individuals discusses a designated topic, leveraging interactive group dynamics to uncover shared attitudes, contrasting norms, and collective perceptions.",
    "best_used_when": "When group synergy and peer reaction help elicit viewpoints that might not emerge during solitary one-on-one interviews, such as product reactions or cultural attitudes.",
    "strengths": [
      "Group interaction stimulates recall and rich debate among peers",
      "Time-efficient way to collect viewpoints from multiple participants simultaneously",
      "Reveals collective agreements, controversies, and cultural vernacular"
    ],
    "limitations": [
      "Dominant individuals may suppress minority or shy opinions",
      "Susceptible to groupthink and peer pressure conformism",
      "Limits confidentiality among participants in the group session"
    ],
    "typical_data_collection": [
      "Multi-speaker audio/video recording of moderated discussions",
      "Co-moderator observational notes on body language and group dynamics",
      "Post-session participant evaluation sheets"
    ],
    "typical_analysis_techniques": [
      "Thematic interaction analysis",
      "Framework analysis",
      "Conversational discourse mapping"
    ],
    "sample_size_guidance": "3 to 6 focus groups, each consisting of 6 to 10 participants (total 20-50 participants).",
    "time_required": "med",
    "cost": "med",
    "ethical_considerations": "Establishing ground rules for respecting participant privacy and mutual confidentiality within the group.",
    "example_use_cases": [
      {
        "domain": "management",
        "title": "Customer Acceptance of AI Customer Service Chatbots",
        "scenario": "Hosting 4 focus groups of e-commerce consumers to observe spontaneous reactions to automated dispute resolution tools."
      },
      {
        "domain": "education",
        "title": "First-Generation College Student Transition Programs",
        "scenario": "Conducting 3 focus groups with incoming freshmen to understand collective emotional barriers and social integration needs."
      }
    ],
    "suitable_domains": [
      "management",
      "education",
      "social science",
      "health"
    ],
    "references": [
      {
        "author": "Krueger, R. A., & Casey, M. A.",
        "year": 2014,
        "title": "Focus Groups: A Practical Guide for Applied Research (5th ed.)",
        "publisher_or_journal": "SAGE Publications"
      },
      {
        "author": "Creswell, J. W., & Creswell, J. D.",
        "year": 2018,
        "title": "Research Design: Qualitative, Quantitative, and Mixed Methods Approaches",
        "publisher_or_journal": "SAGE Publications"
      }
    ]
  },
  {
    "id": "ethnography",
    "name": "Ethnographic Research",
    "category": "qualitative",
    "status": "draft - needs faculty verification",
    "description": "An immersive qualitative design where the researcher engages in sustained participant observation within a natural cultural setting or community to examine shared patterns of values, behaviors, language, and rituals over an extended period.",
    "best_used_when": "When researchers need to understand unwritten cultural practices, workplace micro-cultures, or community norms from an insider (emic) perspective.",
    "strengths": [
      "Unmatched ecological validity and depth of contextual understanding",
      "Uncovers implicit, tacit knowledge that participants cannot articulate on surveys",
      "Reduces discrepancy between what people say they do versus what they actually do"
    ],
    "limitations": [
      "Extremely prolonged commitment required (often months to a year)",
      "Risk of researcher 'going native' and losing analytical objectivity",
      "Difficult to negotiate long-term access to closed cultural settings"
    ],
    "typical_data_collection": [
      "Participant and non-participant field observations",
      "Daily reflective field journals and thick descriptions",
      "Informal conversational interviews and cultural artifact collection"
    ],
    "typical_analysis_techniques": [
      "Thick ethnographic description and cultural interpretation",
      "Domain and taxonomic semantic analysis",
      "Grounded cultural narrative synthesis"
    ],
    "sample_size_guidance": "1 bounded cultural group or community; continuous observation over extended timeframe.",
    "time_required": "high",
    "cost": "high",
    "ethical_considerations": "Navigating covert vs. overt observation ethics, building mutual trust, avoiding cultural exploitation, and protecting informant identities.",
    "example_use_cases": [
      {
        "domain": "social science",
        "title": "Street Vendor Informal Economic Networks in Urban Centers",
        "scenario": "Spending 6 months embedded alongside informal market vendors to understand credit systems and communal solidarity."
      },
      {
        "domain": "engineering",
        "title": "Engineering Culture and Incident Triage in DevOps Squads",
        "scenario": "Shadowing software site reliability teams on-call for 4 months to understand workplace psychological safety and blameless post-mortem practices."
      }
    ],
    "suitable_domains": [
      "social science",
      "engineering",
      "management",
      "education"
    ],
    "references": [
      {
        "author": "Fetterman, D. M.",
        "year": 2019,
        "title": "Ethnography: Step-by-Step (4th ed.)",
        "publisher_or_journal": "SAGE Publications"
      },
      {
        "author": "Creswell, J. W., & Poth, C. N.",
        "year": 2018,
        "title": "Qualitative Inquiry and Research Design: Choosing Among Five Approaches",
        "publisher_or_journal": "SAGE Publications"
      }
    ]
  },
  {
    "id": "grounded_theory",
    "name": "Grounded Theory",
    "category": "qualitative",
    "status": "draft - needs faculty verification",
    "description": "An inductive qualitative methodology in which the researcher generates or develops an abstract conceptual theory of a process, action, or interaction grounded deeply in the views and voices of participants.",
    "best_used_when": "When existing theoretical frameworks are non-existent, inadequate, or fail to explain a novel social phenomenon or human process.",
    "strengths": [
      "Produces systematic, conceptually grounded inductive theories",
      "Explicit, rigorous coding procedures (open, axial, selective coding)",
      "Iterative constant comparative method sharpens construct validity"
    ],
    "limitations": [
      "Demands significant methodological expertise and conceptual abstraction",
      "Generates massive volumes of qualitative text that require meticulous coding",
      "Time-consuming due to simultaneous data collection and theoretical sampling"
    ],
    "typical_data_collection": [
      "Iterative theoretical-sampling interviews",
      "Process-oriented field observations",
      "Extensive analytical and reflexive memo-writing"
    ],
    "typical_analysis_techniques": [
      "Open coding (concept identification)",
      "Axial coding (relating categories to subcategories)",
      "Selective coding (identifying the core conceptual story)",
      "Constant comparative analysis"
    ],
    "sample_size_guidance": "20 to 50 interviews governed by theoretical saturation (no new properties emerging).",
    "time_required": "high",
    "cost": "med",
    "ethical_considerations": "Informed consent, transparency with participants about emerging conceptual models, and anonymization of narrative excerpts.",
    "example_use_cases": [
      {
        "domain": "management",
        "title": "How Tech Startups Pivot in Volatile Macroeconomic Markets",
        "scenario": "Interviewing 32 startup founders iteratively to build a substantive process theory explaining phases of organizational pivoting."
      },
      {
        "domain": "health",
        "title": "Family Caregiver Adaptation to Early-Onset Dementia",
        "scenario": "Developing a conceptual trajectory theory of psychological coping strategies based on iterative interviews with 28 familial caregivers."
      }
    ],
    "suitable_domains": [
      "management",
      "health",
      "social science",
      "education"
    ],
    "references": [
      {
        "author": "Charmaz, K.",
        "year": 2014,
        "title": "Constructing Grounded Theory (2nd ed.)",
        "publisher_or_journal": "SAGE Publications"
      },
      {
        "author": "Corbin, J., & Strauss, A.",
        "year": 2014,
        "title": "Basics of Qualitative Research: Techniques and Procedures for Developing Grounded Theory",
        "publisher_or_journal": "SAGE Publications"
      }
    ]
  },
  {
    "id": "phenomenology",
    "name": "Phenomenological Research",
    "category": "qualitative",
    "status": "draft - needs faculty verification",
    "description": "A qualitative design that investigates the common meaning for several individuals of their lived experiences of a specific concept or phenomenon, aiming to distill the universal essence of that experience.",
    "best_used_when": "When the research goal is to understand the deep, subjective, emotional essence of how human beings experience a shared life event or condition.",
    "strengths": [
      "Uncovers rich, profound descriptions of human consciousness and lived meaning",
      "Honors the subjective experiences of participants without imposing preconceptions",
      "Brings clarity to deeply personal, transformative, or traumatic human experiences"
    ],
    "limitations": [
      "Requires researchers to bracket (epoche) their own personal assumptions and biases",
      "Not intended for statistical generalization or causal modeling",
      "Can be emotionally taxing on both researcher and participants"
    ],
    "typical_data_collection": [
      "In-depth, contemplative open interviews (1-2 hours each)",
      "Participant written reflections, diaries, or creative narratives",
      "Researcher bracketing memos"
    ],
    "typical_analysis_techniques": [
      "Moustakas phenomenological reduction",
      "Horizontalization (treating all statements with equal value)",
      "Synthesis of textural ('what') and structural ('how') descriptions into an essence"
    ],
    "sample_size_guidance": "5 to 15 participants who have all experienced the core phenomenon under study.",
    "time_required": "med",
    "cost": "low",
    "ethical_considerations": "Heightened psychological sensitivity, ensuring access to counseling resources if interviews trigger traumatic memories, and maintaining strict confidentiality.",
    "example_use_cases": [
      {
        "domain": "education",
        "title": "The Lived Experience of Sudden Transition to Remote Learning",
        "scenario": "Exploring the emotional and cognitive essences of 10 university students forced to transition entirely to solitary online education during lockdowns."
      },
      {
        "domain": "health",
        "title": "Living with Sudden Sensorineural Hearing Loss",
        "scenario": "Investigating the fundamental psychological shift in self-identity and communication among 8 adults diagnosed with acute hearing loss."
      }
    ],
    "suitable_domains": [
      "health",
      "education",
      "social science"
    ],
    "references": [
      {
        "author": "Moustakas, C.",
        "year": 1994,
        "title": "Phenomenological Research Methods",
        "publisher_or_journal": "SAGE Publications"
      },
      {
        "author": "Creswell, J. W., & Poth, C. N.",
        "year": 2018,
        "title": "Qualitative Inquiry and Research Design: Choosing Among Five Approaches",
        "publisher_or_journal": "SAGE Publications"
      }
    ]
  },
  {
    "id": "content_analysis",
    "name": "Content Analysis",
    "category": "mixed",
    "status": "draft - needs faculty verification",
    "description": "A systematic, replicable research technique for compressing many words of text, images, or media into fewer content categories based on explicit rules of coding, which can be qualitative (thematic/relational) or quantitative (frequency/word counts).",
    "best_used_when": "When analyzing documented communication artifacts (transcripts, news articles, social media posts, corporate annual reports) without direct participant contact.",
    "strengths": [
      "Non-invasive and unobtrusive; does not alter participant behavior",
      "Enables historical and longitudinal text analysis across decades",
      "Can bridge qualitative meaning and quantitative statistical metrics"
    ],
    "limitations": [
      "Constrained purely to recorded communications; cannot question the author",
      "Risk of misinterpreting the author's intended tone, humor, or context",
      "Requires rigorous inter-coder reliability checks to avoid subjective coding drift"
    ],
    "typical_data_collection": [
      "Web scraping of social media threads or customer reviews",
      "Archival corporate disclosures, legal briefs, or news articles",
      "Syllabi, policy documentation, or video transcripts"
    ],
    "typical_analysis_techniques": [
      "Automated dictionary-based word frequency counts",
      "Qualitative relational and conceptual thematic coding",
      "Krippendorff's Alpha or Fleiss' Kappa inter-coder reliability testing"
    ],
    "sample_size_guidance": "Dozens of qualitative documents to thousands/millions of digital posts or sentences.",
    "time_required": "med",
    "cost": "low",
    "ethical_considerations": "Respecting digital terms of service, fair use of public online discourse, and avoiding deanonymization of vulnerable online posters.",
    "example_use_cases": [
      {
        "domain": "management",
        "title": "Greenwashing Claims in Corporate ESG Sustainability Reports",
        "scenario": "Coding 150 corporate annual sustainability reports from Fortune 500 firms to quantify discrepancies between environmental promises and tangible audits."
      },
      {
        "domain": "social science",
        "title": "Public Sentiment Regarding Vaccination on Social Platforms",
        "scenario": "Analyzing 5,000 public microblog posts to categorize moral framing, skepticism themes, and authoritative source citation."
      }
    ],
    "suitable_domains": [
      "management",
      "social science",
      "education",
      "health"
    ],
    "references": [
      {
        "author": "Krippendorff, K.",
        "year": 2018,
        "title": "Content Analysis: An Introduction to Its Methodology (4th ed.)",
        "publisher_or_journal": "SAGE Publications"
      },
      {
        "author": "Neuendorf, K. A.",
        "year": 2017,
        "title": "The Content Analysis Guidebook (2nd ed.)",
        "publisher_or_journal": "SAGE Publications"
      }
    ]
  },
  {
    "id": "systematic_literature_review",
    "name": "Systematic Literature Review",
    "category": "mixed",
    "status": "draft - needs faculty verification",
    "description": "A rigorous, transparent, and reproducible methodology to identify, select, critically appraise, and synthesize all relevant empirical research on a clearly formulated research question, following standardized reporting protocols (e.g., PRISMA).",
    "best_used_when": "When researchers aim to consolidate the existing body of evidence, identify methodological gaps, or reconcile conflicting findings across existing literature.",
    "strengths": [
      "Transparent, auditable, and repeatable search protocol minimizes publication bias",
      "Synthesizes entire fields of prior research without requiring new primary participant recruitment",
      "High scientific impact and authoritative benchmark for future research agendas"
    ],
    "limitations": [
      "Labor-intensive screening of hundreds or thousands of database citations",
      "Vulnerable to publication bias (studies with null results are under-published)",
      "Requires access to comprehensive academic subscription databases (Scopus, Web of Science, IEEE Xplore)"
    ],
    "typical_data_collection": [
      "Boolean keyword queries across indexed bibliographic databases",
      "Documented inclusion/exclusion eligibility screening logs",
      "Standardized data extraction templates and quality assessment rubrics"
    ],
    "typical_analysis_techniques": [
      "PRISMA flow diagram generation",
      "Risk of bias and study quality appraisal (CASP, Cochrane RoB)",
      "Narrative and tabular evidence synthesis"
    ],
    "sample_size_guidance": "Typically 30 to 100 included peer-reviewed empirical studies selected from initial pool of thousands.",
    "time_required": "high",
    "cost": "low",
    "ethical_considerations": "Proper attribution, transparent disclosure of funding sources, avoidance of cherry-picking, and adherence to PRISMA reporting standards.",
    "example_use_cases": [
      {
        "domain": "engineering",
        "title": "Static Code Analysis Tools for Detecting Cybersecurity Vulnerabilities",
        "scenario": "Systematically reviewing 65 empirical studies evaluating the precision and recall of open-source static analyzers against CWE vulnerabilities."
      },
      {
        "domain": "education",
        "title": "Gamification Interventions in Higher Education STEM Disciplines",
        "scenario": "Synthesizing 42 empirical classroom interventions to assess the impact of leaderboards and digital badges on student engagement."
      }
    ],
    "suitable_domains": [
      "engineering",
      "education",
      "health",
      "management",
      "social science"
    ],
    "references": [
      {
        "author": "Page, M. J., et al.",
        "year": 2021,
        "title": "The PRISMA 2020 statement: an updated guideline for reporting systematic reviews",
        "publisher_or_journal": "BMJ, 372(n71)"
      },
      {
        "author": "Kitchenham, B., & Charters, S.",
        "year": 2007,
        "title": "Guidelines for performing Systematic Literature Reviews in Software Engineering",
        "publisher_or_journal": "Keele University and Durham University Joint Report"
      }
    ]
  },
  {
    "id": "meta_analysis",
    "name": "Meta-Analysis",
    "category": "quantitative",
    "status": "draft - needs faculty verification",
    "description": "A quantitative, statistical synthesis that combines the numerical results of multiple independent empirical studies addressing the same research question to calculate a single pooled effect size and evaluate heterogeneity.",
    "best_used_when": "When multiple quantitative studies with conflicting or ambiguous effect sizes exist, and the researcher wishes to establish definitive statistical effect sizes.",
    "strengths": [
      "Substantially increases statistical power and precision over individual studies",
      "Quantifies and explains heterogeneity across disparate populations and study designs",
      "Evaluates publication bias through funnel plots and Egger's regression"
    ],
    "limitations": [
      "Garbage-in, garbage-out: vulnerable to poor methodology in primary studies",
      "'Apples and oranges' dilemma when combining dissimilar interventions",
      "Requires deep quantitative and statistical modeling expertise"
    ],
    "typical_data_collection": [
      "Extraction of sample sizes, means, standard deviations, odds ratios, and p-values from published studies",
      "Systematic retrieval of unpublished dissertations to combat publication bias"
    ],
    "typical_analysis_techniques": [
      "Fixed-effects and random-effects statistical pooling (Hedges' g, Cohen's d)",
      "Heterogeneity testing (Cochran's Q and I-squared statistic)",
      "Meta-regression and subgroup moderation analysis"
    ],
    "sample_size_guidance": "Minimum 10 to 30 homogeneous quantitative empirical studies reporting sufficient numerical data.",
    "time_required": "high",
    "cost": "low",
    "ethical_considerations": "Rigorous transparency in statistical criteria, avoiding selective inclusion to artificially alter pooled effect sizes.",
    "example_use_cases": [
      {
        "domain": "health",
        "title": "Cardiorespiratory Fitness Benefits of High-Intensity Interval Training (HIIT)",
        "scenario": "Pooling numerical VO2 max gains across 28 randomized trials comparing HIIT to steady-state endurance cardio in middle-aged adults."
      },
      {
        "domain": "management",
        "title": "Relationship Between Transformational Leadership and Team Performance",
        "scenario": "Conducting a meta-analysis on 45 quantitative organizational studies to derive the true population correlation coefficient."
      }
    ],
    "suitable_domains": [
      "health",
      "management",
      "education",
      "social science"
    ],
    "references": [
      {
        "author": "Borenstein, M., Hedges, L. V., Higgins, J. P., & Rothstein, H. R.",
        "year": 2021,
        "title": "Introduction to Meta-Analysis (2nd ed.)",
        "publisher_or_journal": "John Wiley & Sons"
      },
      {
        "author": "Creswell, J. W., & Creswell, J. D.",
        "year": 2018,
        "title": "Research Design: Qualitative, Quantitative, and Mixed Methods Approaches",
        "publisher_or_journal": "SAGE Publications"
      }
    ]
  },
  {
    "id": "action_research",
    "name": "Action Research",
    "category": "mixed",
    "status": "draft - needs faculty verification",
    "description": "A collaborative, reflective, and iterative inquiry methodology conducted by practitioners in their own professional context, following a cyclical spiral of planning, acting, observing, and reflecting to resolve immediate practical problems.",
    "best_used_when": "When practitioners seek to improve their own professional practice, implement organizational change, and generate practical knowledge simultaneously.",
    "strengths": [
      "Direct, immediate practical relevance and benefit to participants",
      "Empowers practitioners and fosters collaborative problem solving",
      "Iterative feedback loops allow real-time adaptive interventions"
    ],
    "limitations": [
      "Subject to practitioner confirmation bias and dual-role conflict",
      "Context-specific; findings are rarely generalizable to other institutions",
      "Requires strong institutional support and participant buy-in"
    ],
    "typical_data_collection": [
      "Practitioner reflective logs and teaching/workplace diaries",
      "Participant feedback surveys and focus groups",
      "Operational metrics before and after iterative interventions"
    ],
    "typical_analysis_techniques": [
      "Iterative reflective synthesis",
      "Before-and-after descriptive metric comparisons",
      "Participatory thematic analysis"
    ],
    "sample_size_guidance": "1 bounded classroom, clinic, or team (typically 15-50 stakeholders involved).",
    "time_required": "high",
    "cost": "low",
    "ethical_considerations": "Managing power dynamics when the researcher is also the manager, educator, or clinician of the participants.",
    "example_use_cases": [
      {
        "domain": "education",
        "title": "Improving Coding Comprehension Through Peer Instruction in High School CS",
        "scenario": "A computer science educator runs three successive 4-week action research cycles testing peer instruction in their own classroom."
      },
      {
        "domain": "health",
        "title": "Streamlining Surgical Hand-off Protocols in a Community Hospital",
        "scenario": "A charge nurse collaborates with surgical staff over two quarters to cycle through, test, and refine surgical handover checklists."
      }
    ],
    "suitable_domains": [
      "education",
      "health",
      "management"
    ],
    "references": [
      {
        "author": "Stringer, E. T.",
        "year": 2014,
        "title": "Action Research (4th ed.)",
        "publisher_or_journal": "SAGE Publications"
      },
      {
        "author": "Saunders, M., Lewis, P., & Thornhill, A.",
        "year": 2019,
        "title": "Research Methods for Business Students",
        "publisher_or_journal": "Pearson Education"
      }
    ]
  },
  {
    "id": "design_science_research",
    "name": "Design Science Research",
    "category": "mixed",
    "status": "draft - needs faculty verification",
    "description": "A constructive, problem-solving paradigm rooted in engineering and informatics that creates and evaluates novel innovative IT/engineering artifacts (algorithms, models, architectures, systems) to solve identified real-world problems.",
    "best_used_when": "When the primary research objective is to invent, build, and rigorously evaluate a novel technology, software architecture, algorithm, or operational prototype.",
    "strengths": [
      "Produces actionable, tangible intellectual property and technological solutions",
      "Bridges theoretical rigor with engineering utility and innovation",
      "Directly aligns with software, systems, and engineering design cycles"
    ],
    "limitations": [
      "Demands high technical proficiency and development effort",
      "Evaluation may be biased if the artifact developer is also the sole evaluator",
      "Risk of over-focusing on building at the expense of scholarly contribution"
    ],
    "typical_data_collection": [
      "System performance telemetry (throughput, latency, CPU utilization)",
      "Heuristic usability walkthroughs and developer task evaluations",
      "Benchmark dataset accuracy runs and comparative profiling"
    ],
    "typical_analysis_techniques": [
      "Comparative algorithmic benchmarking",
      "Usability metric analysis (System Usability Scale - SUS)",
      "A/B performance testing against baseline architectures"
    ],
    "sample_size_guidance": "Varies: 1 novel system prototype benchmarked against standard datasets or evaluated with 15-30 targeted technical users.",
    "time_required": "high",
    "cost": "med",
    "ethical_considerations": "Software security, algorithmic fairness, software licensing compliance, and user safety when testing automated systems.",
    "example_use_cases": [
      {
        "domain": "engineering",
        "title": "Federated Learning Framework for Privacy-Preserving IoT Anomaly Detection",
        "scenario": "Designing, implementing, and benchmarking a novel decentralized algorithm across simulated edge hardware nodes."
      },
      {
        "domain": "management",
        "title": "Decision Support System for Resilient Supply Chain Disruption Management",
        "scenario": "Developing a graph-based simulation artifact and evaluating it with supply chain managers in pharmaceutical logistics."
      }
    ],
    "suitable_domains": [
      "engineering",
      "management"
    ],
    "references": [
      {
        "author": "Hevner, A. R., March, S. T., Park, J., & Ram, S.",
        "year": 2004,
        "title": "Design Science in Information Systems Research",
        "publisher_or_journal": "MIS Quarterly, 28(1), 75-105"
      },
      {
        "author": "Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S.",
        "year": 2007,
        "title": "A Design Science Research Methodology for Information Systems Research",
        "publisher_or_journal": "Journal of Management Information Systems, 24(3), 45-77"
      }
    ]
  },
  {
    "id": "mixed_methods",
    "name": "Mixed Methods (Convergent/Sequential)",
    "category": "mixed",
    "status": "draft - needs faculty verification",
    "description": "A research design that intentionally integrates both quantitative and qualitative research paradigms within a single study or program of inquiry to provide a more complete, comprehensive understanding than either approach alone.",
    "best_used_when": "When quantitative numbers alone leave the 'why' unexplained, or qualitative insights require broader empirical generalization.",
    "strengths": [
      "Offers both breadth (statistical power) and depth (lived experience)",
      "Triangulation corroborates findings across distinct methodologies",
      "Compensates for the weaknesses of single-paradigm approaches"
    ],
    "limitations": [
      "Resource-intensive: requires expertise in both statistical and qualitative methods",
      "Complex data integration challenges when quant and qual results diverge",
      "Longer timeframes required to collect and integrate multi-modal data"
    ],
    "typical_data_collection": [
      "Simultaneous or sequential surveys and semi-structured qualitative interviews",
      "Quantitative sensor logs paired with qualitative participant diary reflections"
    ],
    "typical_analysis_techniques": [
      "Joint display matrices integrating qualitative themes with survey statistics",
      "Data transformation (quantitizing qualitative themes or qualitizing stats)",
      "Exploratory sequential or explanatory sequential modeling"
    ],
    "sample_size_guidance": "100+ for the quantitative survey phase; 15-25 for the qualitative interview phase.",
    "time_required": "high",
    "cost": "med",
    "ethical_considerations": "Dual consent protocols, managing participant burden across multiple sessions, and ensuring consistency across phases.",
    "example_use_cases": [
      {
        "domain": "education",
        "title": "Student Engagement in Virtual Reality Labs",
        "scenario": "Collecting survey telemetry from 180 physics undergraduates followed by in-depth explanatory interviews with 15 outliers."
      },
      {
        "domain": "health",
        "title": "Telemedicine Adoption in Rural Primary Clinics",
        "scenario": "Conducting a statewide clinic survey (n=120) paired with 4 contextual focus groups of rural healthcare providers."
      }
    ],
    "suitable_domains": [
      "education",
      "health",
      "management",
      "social science"
    ],
    "references": [
      {
        "author": "Creswell, J. W., & Creswell, J. D.",
        "year": 2018,
        "title": "Research Design: Qualitative, Quantitative, and Mixed Methods Approaches",
        "publisher_or_journal": "SAGE Publications"
      },
      {
        "author": "Teddlie, C., & Tashakkori, A.",
        "year": 2009,
        "title": "Foundations of Mixed Methods Research",
        "publisher_or_journal": "SAGE Publications"
      }
    ]
  },
  {
    "id": "delphi_technique",
    "name": "Delphi Technique",
    "category": "mixed",
    "status": "draft - needs faculty verification",
    "description": "A structured, iterative communication and forecasting process that seeks to reach consensus among a panel of geographically dispersed subject matter experts through multiple rounds of questionnaires with controlled anonymous feedback.",
    "best_used_when": "When empirical historical data is lacking and expert consensus is required for forecasting, policy formulation, curriculum design, or indicator development.",
    "strengths": [
      "Overcomes groupthink and dominant personalities through panelist anonymity",
      "Engages leading domain experts across continents without travel costs",
      "Structured rounds allow experts to re-evaluate their views based on group feedback"
    ],
    "limitations": [
      "Panelist attrition (expert dropout) over successive rounds threatens validity",
      "Lengthy multi-round process (can take 2-4 months)",
      "Arbitrary consensus thresholds (e.g., 70% or 80% agreement definition)"
    ],
    "typical_data_collection": [
      "Round 1: Open-ended qualitative questionnaires to generate items",
      "Round 2 & 3: Rating scales (Likert) with statistical summaries of previous rounds"
    ],
    "typical_analysis_techniques": [
      "Interquartile range (IQR) and standard deviation consensus tracking",
      "Content analysis of round 1 expert contributions",
      "Kendall's W coefficient of concordance"
    ],
    "sample_size_guidance": "15 to 35 qualified domain experts.",
    "time_required": "high",
    "cost": "low",
    "ethical_considerations": "Strict protection of expert panel anonymity between rounds, preventing coercion to conform.",
    "example_use_cases": [
      {
        "domain": "health",
        "title": "Core Competencies for Emergency Pandemic Response Nurses",
        "scenario": "Conducting a 3-round Delphi study with 25 international epidemiology and nursing leaders to standardize training criteria."
      },
      {
        "domain": "engineering",
        "title": "Defining Critical Success Factors for AI in Avionics Systems",
        "scenario": "Engaging 20 aerospace systems architects over three questionnaire iterations to establish safety certification guidelines."
      }
    ],
    "suitable_domains": [
      "health",
      "engineering",
      "management",
      "education"
    ],
    "references": [
      {
        "author": "Linstone, H. A., & Turoff, M.",
        "year": 1975,
        "title": "The Delphi Method: Techniques and Applications",
        "publisher_or_journal": "Addison-Wesley"
      },
      {
        "author": "Saunders, M., Lewis, P., & Thornhill, A.",
        "year": 2019,
        "title": "Research Methods for Business Students",
        "publisher_or_journal": "Pearson Education"
      }
    ]
  },
  {
    "id": "longitudinal_study",
    "name": "Longitudinal Study",
    "category": "quantitative",
    "status": "draft - needs faculty verification",
    "description": "An observational research design that repeatedly measures the same subjects or cohort over an extended chronological period (months to years) to track development, trajectory changes, and temporal patterns.",
    "best_used_when": "When research requires establishing the temporal sequence of events, tracking developmental changes over time, or studying long-term trends.",
    "strengths": [
      "Uniquely captures temporal sequencing, development, and maturation",
      "Distinguishes short-term fluctuations from enduring developmental trajectories",
      "Eliminates cohort effects present in cross-sectional comparisons"
    ],
    "limitations": [
      "High participant attrition (dropouts) over time which biases sample representativeness",
      "Very high time commitment and financial expense",
      "Testing effects: repeated exposure to tests can alter participant performance"
    ],
    "typical_data_collection": [
      "Repeated periodic surveys or clinical assessments across discrete time intervals (T1, T2, T3)",
      "Electronic biometric wearable monitoring over months",
      "Annual institutional registry audits"
    ],
    "typical_analysis_techniques": [
      "Repeated-measures ANOVA / Latent Growth Curve Modeling",
      "Linear Mixed-Effects Models (Hierarchical Linear Modeling - HLM)",
      "Survival analysis and hazard rate estimation"
    ],
    "sample_size_guidance": "100+ baseline participants to withstand 20-40% projected longitudinal attrition.",
    "time_required": "high",
    "cost": "high",
    "ethical_considerations": "Maintaining participant re-consent over extended durations, secure long-term tracking of personal contact details.",
    "example_use_cases": [
      {
        "domain": "health",
        "title": "Cognitive Decline and Physical Activity in Aging Cohorts",
        "scenario": "Tracking cognitive assessments and accelerometer activity in 250 older adults at 6-month intervals over 3 years."
      },
      {
        "domain": "education",
        "title": "Career Trajectories of Underrepresented Engineering Graduates",
        "scenario": "Following 150 alumni at graduation, year 1, year 3, and year 5 to study workplace retention and career milestones."
      }
    ],
    "suitable_domains": [
      "health",
      "education",
      "social science"
    ],
    "references": [
      {
        "author": "Singer, J. D., & Willett, J. B.",
        "year": 2003,
        "title": "Applied Longitudinal Data Analysis: Modeling Change and Event Occurrence",
        "publisher_or_journal": "Oxford University Press"
      },
      {
        "author": "Kothari, C. R.",
        "year": 2004,
        "title": "Research Methodology: Methods and Techniques",
        "publisher_or_journal": "New Age International Publishers"
      }
    ]
  },
  {
    "id": "cross_sectional_study",
    "name": "Cross-Sectional Study",
    "category": "quantitative",
    "status": "draft - needs faculty verification",
    "description": "An observational study design in which data is gathered from a defined population, or a representative subset, at a single specific point in time to examine the prevalence of characteristics or associations between variables.",
    "best_used_when": "When researchers need a rapid, cost-effective snapshot of prevalence, distribution, or associations within a population without following subjects over time.",
    "strengths": [
      "Relatively rapid, efficient, and cost-effective compared to longitudinal tracking",
      "Provides valuable estimates of disease or phenomenon prevalence in populations",
      "Can examine multiple outcomes and exposures simultaneously"
    ],
    "limitations": [
      "Cannot establish temporal precedence (chicken-or-egg problem); cannot infer causality",
      "Susceptible to survivorship and recall bias",
      "Confounded by cohort generation differences when comparing age groups"
    ],
    "typical_data_collection": [
      "One-time digital questionnaires or standardized field assessments",
      "Point-in-time clinical screenings or health metrics",
      "Single-quarter financial and organizational survey records"
    ],
    "typical_analysis_techniques": [
      "Prevalence calculations and Odds Ratios (OR)",
      "Multivariable logistic regression",
      "Chi-square contingency tests and Mann-Whitney U tests"
    ],
    "sample_size_guidance": "100 to 500+ respondents depending on expected population prevalence.",
    "time_required": "low",
    "cost": "low",
    "ethical_considerations": "Informed consent, voluntary participation, and non-disclosure of individual clinical or sensitive survey results.",
    "example_use_cases": [
      {
        "domain": "health",
        "title": "Prevalence of Ergonomic Repetitive Strain Injuries Among Software Engineers",
        "scenario": "Surveying 300 programmers across tech parks during Q2 to determine the prevalence of carpal tunnel symptoms and desk setup."
      },
      {
        "domain": "management",
        "title": "Financial Literacy and Investment Propensity Among Gen Z Professionals",
        "scenario": "Administering a one-time questionnaire to 400 young professionals to evaluate correlations between financial knowledge and crypto investment."
      }
    ],
    "suitable_domains": [
      "health",
      "management",
      "social science",
      "education"
    ],
    "references": [
      {
        "author": "Creswell, J. W., & Creswell, J. D.",
        "year": 2018,
        "title": "Research Design: Qualitative, Quantitative, and Mixed Methods Approaches",
        "publisher_or_journal": "SAGE Publications"
      },
      {
        "author": "Saunders, M., Lewis, P., & Thornhill, A.",
        "year": 2019,
        "title": "Research Methods for Business Students",
        "publisher_or_journal": "Pearson Education"
      }
    ]
  },
  {
    "id": "correlational_study",
    "name": "Correlational Research",
    "category": "quantitative",
    "status": "draft - needs faculty verification",
    "description": "A non-experimental quantitative design that investigates the statistical relationship between two or more variables without manipulating the independent variable or exerting experimental control.",
    "best_used_when": "When experimental manipulation is impossible, unethical, or impractical, but establishing the strength and direction of predictive relationships is crucial.",
    "strengths": [
      "Identifies strength and direction of associations between variables",
      "Facilitates mathematical predictive modeling",
      "Highly feasible using existing or naturalistic datasets"
    ],
    "limitations": [
      "Correlation does not imply causation (omitted variable and third-variable problem)",
      "Directionality problem: unclear whether variable X causes Y or Y causes X",
      "Susceptible to spurious correlations in large observational datasets"
    ],
    "typical_data_collection": [
      "Standardized multi-item scales and numerical questionnaires",
      "Secondary historical databases and academic records",
      "Sensor or usage log telemetry"
    ],
    "typical_analysis_techniques": [
      "Pearson's r and Spearman's rho correlation coefficients",
      "Multiple linear and polynomial regression",
      "Structural Equation Modeling (SEM) and path analysis"
    ],
    "sample_size_guidance": "80 to 250+ cases for robust multiple regression power.",
    "time_required": "low",
    "cost": "low",
    "ethical_considerations": "Responsible interpretation of statistical correlations to prevent misleading causal claims to the public.",
    "example_use_cases": [
      {
        "domain": "education",
        "title": "Predicting Academic Retention from Library Resource Utilization",
        "scenario": "Analyzing the statistical correlation between student digital library log-ins and second-year retention rates across 500 undergraduates."
      },
      {
        "domain": "management",
        "title": "CEO Social Media Activity and Short-Term Stock Volatility",
        "scenario": "Examining 2 years of daily CEO Twitter postings correlated with daily trading volume across 100 publicly traded tech firms."
      }
    ],
    "suitable_domains": [
      "education",
      "management",
      "social science",
      "health"
    ],
    "references": [
      {
        "author": "Kothari, C. R.",
        "year": 2004,
        "title": "Research Methodology: Methods and Techniques",
        "publisher_or_journal": "New Age International Publishers"
      },
      {
        "author": "Creswell, J. W., & Creswell, J. D.",
        "year": 2018,
        "title": "Research Design: Qualitative, Quantitative, and Mixed Methods Approaches",
        "publisher_or_journal": "SAGE Publications"
      }
    ]
  },
  {
    "id": "observational_study",
    "name": "Observational Study",
    "category": "mixed",
    "status": "draft - needs faculty verification",
    "description": "A non-experimental research method where the researcher systematically observes, codes, and records the behavior of subjects in their natural or semi-controlled setting without intervention or manipulation.",
    "best_used_when": "When self-report surveys might be unreliable or when naturalistic behavioral interactions must be recorded exactly as they occur in real time.",
    "strengths": [
      "Captures authentic real-time behavior without relying on participant memory",
      "High ecological validity in naturalistic environments",
      "Effective for populations unable to complete surveys (infants, animals, clinical patients)"
    ],
    "limitations": [
      "Hawthorne effect: subjects may alter behavior when they realize they are observed",
      "Observer bias in interpreting ambiguous interactions",
      "Cannot ascertain internal thoughts, motivations, or private cognitive processes"
    ],
    "typical_data_collection": [
      "Systematic structured observation check-sheets with interval timing",
      "Video recording of human-system or interpersonal interactions",
      "Automated movement trackers or gaze/eye-tracking monitors"
    ],
    "typical_analysis_techniques": [
      "Inter-rater reliability of behavioral coding (Cohen's Kappa)",
      "Behavioral frequency and duration analysis",
      "Sequence analysis of behavioral transitions"
    ],
    "sample_size_guidance": "20 to 60 behavioral sessions or observational intervals.",
    "time_required": "med",
    "cost": "med",
    "ethical_considerations": "Ensuring observational ethics in public vs. semi-private spaces; consent for video recording.",
    "example_use_cases": [
      {
        "domain": "education",
        "title": "Collaborative Problem Solving in Kindergarten Robotics Clubs",
        "scenario": "Observing and coding turn-taking behaviors and conflict resolution among 30 children working in pairs with programmable toy robots."
      },
      {
        "domain": "engineering",
        "title": "Human Factors Usability in Nuclear Control Room Simulators",
        "scenario": "Recording operator eye fixations and hand movements during simulated alarm emergency scenarios."
      }
    ],
    "suitable_domains": [
      "education",
      "engineering",
      "health",
      "social science"
    ],
    "references": [
      {
        "author": "Kothari, C. R.",
        "year": 2004,
        "title": "Research Methodology: Methods and Techniques",
        "publisher_or_journal": "New Age International Publishers"
      },
      {
        "author": "Saunders, M., Lewis, P., & Thornhill, A.",
        "year": 2019,
        "title": "Research Methods for Business Students",
        "publisher_or_journal": "Pearson Education"
      }
    ]
  }
];
const RULES_DATA = [
  {
    "id": "RULE_OBJ_EXPLORE_GT",
    "method_id": "grounded_theory",
    "conditions": {
      "research_objective": "explore"
    },
    "effect": "boost",
    "weight": 35,
    "reason_text": "Grounded Theory is ideally suited for exploratory inquiries seeking to discover emergent conceptual patterns without preconceived hypotheses."
  },
  {
    "id": "RULE_OBJ_EXPLORE_PHENOM",
    "method_id": "phenomenology",
    "conditions": {
      "research_objective": "explore"
    },
    "effect": "boost",
    "weight": 30,
    "reason_text": "Phenomenology excels at exploring the lived essence and deep meanings of human experiences."
  },
  {
    "id": "RULE_OBJ_EXPLORE_CASE",
    "method_id": "case_study",
    "conditions": {
      "research_objective": "explore"
    },
    "effect": "boost",
    "weight": 25,
    "reason_text": "Case study research is highly effective for exploring contemporary phenomena deeply embedded within their real-world context."
  },
  {
    "id": "RULE_OBJ_EXPLORE_ETHNO",
    "method_id": "ethnography",
    "conditions": {
      "research_objective": "explore"
    },
    "effect": "boost",
    "weight": 25,
    "reason_text": "Ethnography provides deep exploratory immersion into cultural norms and social group behaviors."
  },
  {
    "id": "RULE_OBJ_DESCRIBE_SURVEY",
    "method_id": "survey",
    "conditions": {
      "research_objective": "describe"
    },
    "effect": "boost",
    "weight": 35,
    "reason_text": "Survey research is standard for describing prevailing characteristics, attitudes, and distributions across target populations."
  },
  {
    "id": "RULE_OBJ_DESCRIBE_CROSS_SECT",
    "method_id": "cross_sectional_study",
    "conditions": {
      "research_objective": "describe"
    },
    "effect": "boost",
    "weight": 30,
    "reason_text": "Cross-sectional designs provide rapid descriptive snapshots of population prevalence and demographic patterns."
  },
  {
    "id": "RULE_OBJ_DESCRIBE_CONTENT",
    "method_id": "content_analysis",
    "conditions": {
      "research_objective": "describe"
    },
    "effect": "boost",
    "weight": 25,
    "reason_text": "Content analysis provides systematic descriptive categorization of recorded communication artifacts and public text."
  },
  {
    "id": "RULE_OBJ_HYPOTHESIS_EXPERIMENT",
    "method_id": "experiment",
    "conditions": {
      "research_objective": "explain_test_hypothesis"
    },
    "effect": "boost",
    "weight": 40,
    "reason_text": "True experimental design is the benchmark method for testing causal hypotheses with maximum internal validity."
  },
  {
    "id": "RULE_OBJ_HYPOTHESIS_QUASI",
    "method_id": "quasi_experiment",
    "conditions": {
      "research_objective": "explain_test_hypothesis"
    },
    "effect": "boost",
    "weight": 30,
    "reason_text": "Quasi-experiments test causal hypotheses in naturalistic settings where true random assignment is infeasible."
  },
  {
    "id": "RULE_OBJ_HYPOTHESIS_CORRELATIONAL",
    "method_id": "correlational_study",
    "conditions": {
      "research_objective": "explain_test_hypothesis"
    },
    "effect": "boost",
    "weight": 25,
    "reason_text": "Correlational research evaluates directional hypotheses regarding statistical relationships between variables."
  },
  {
    "id": "RULE_OBJ_PREDICT_CORRELATIONAL",
    "method_id": "correlational_study",
    "conditions": {
      "research_objective": "predict"
    },
    "effect": "boost",
    "weight": 40,
    "reason_text": "Correlational regression designs directly assess predictive relationships between predictor and criterion variables."
  },
  {
    "id": "RULE_OBJ_PREDICT_LONGITUDINAL",
    "method_id": "longitudinal_study",
    "conditions": {
      "research_objective": "predict"
    },
    "effect": "boost",
    "weight": 30,
    "reason_text": "Longitudinal designs establish temporal precedence required for robust predictive and developmental forecasting."
  },
  {
    "id": "RULE_OBJ_INTERVENTION_EXP",
    "method_id": "experiment",
    "conditions": {
      "research_objective": "evaluate_intervention"
    },
    "effect": "boost",
    "weight": 35,
    "reason_text": "Randomized experimental trials isolate intervention treatment effects against a control baseline."
  },
  {
    "id": "RULE_OBJ_INTERVENTION_QUASI",
    "method_id": "quasi_experiment",
    "conditions": {
      "research_objective": "evaluate_intervention"
    },
    "effect": "boost",
    "weight": 35,
    "reason_text": "Quasi-experimental pre/post designs are ideally tailored for evaluating organizational, classroom, or community interventions."
  },
  {
    "id": "RULE_OBJ_INTERVENTION_ACTION",
    "method_id": "action_research",
    "conditions": {
      "research_objective": "evaluate_intervention"
    },
    "effect": "boost",
    "weight": 35,
    "reason_text": "Action research engages practitioners in iterative cycles of implementing and refining interventions directly within their practice."
  },
  {
    "id": "RULE_OBJ_ARTIFACT_DSR",
    "method_id": "design_science_research",
    "conditions": {
      "research_objective": "build_evaluate_artifact"
    },
    "effect": "boost",
    "weight": 45,
    "reason_text": "Design Science Research (DSR) is the established paradigm for creating and rigorously evaluating novel engineering, IT, or architectural artifacts."
  },
  {
    "id": "RULE_OBJ_ARTIFACT_EXP",
    "method_id": "experiment",
    "conditions": {
      "research_objective": "build_evaluate_artifact"
    },
    "effect": "boost",
    "weight": 20,
    "reason_text": "Controlled experiments benchmark the technical performance of novel engineered systems and algorithms."
  },
  {
    "id": "RULE_OBJ_LITERATURE_SLR",
    "method_id": "systematic_literature_review",
    "conditions": {
      "research_objective": "review_literature"
    },
    "effect": "boost",
    "weight": 45,
    "reason_text": "Systematic Literature Review (SLR/PRISMA) provides an auditable, comprehensive protocol for synthesizing existing empirical evidence."
  },
  {
    "id": "RULE_OBJ_LITERATURE_META",
    "method_id": "meta_analysis",
    "conditions": {
      "research_objective": "review_literature"
    },
    "effect": "boost",
    "weight": 35,
    "reason_text": "Meta-analysis quantitatively synthesizes numerical effect sizes across a body of published quantitative studies."
  },
  {
    "id": "RULE_DATA_NUMERICAL_QUANT_BOOST",
    "method_id": "experiment",
    "conditions": {
      "data_type": "numerical"
    },
    "effect": "boost",
    "weight": 25,
    "reason_text": "Your focus on numerical metrics strongly aligns with quantitative experimental measurement."
  },
  {
    "id": "RULE_DATA_NUMERICAL_SURVEY_BOOST",
    "method_id": "survey",
    "conditions": {
      "data_type": "numerical"
    },
    "effect": "boost",
    "weight": 20,
    "reason_text": "Numerical rating scales and Likert inventories match standardized survey analysis."
  },
  {
    "id": "RULE_DATA_NUMERICAL_QUAL_PENALTY",
    "method_id": "phenomenology",
    "conditions": {
      "data_type": "numerical"
    },
    "effect": "penalty",
    "weight": 30,
    "reason_text": "Phenomenology requires deep rich narrative transcripts rather than strictly numerical data."
  },
  {
    "id": "RULE_DATA_NUMERICAL_GT_PENALTY",
    "method_id": "grounded_theory",
    "conditions": {
      "data_type": "numerical"
    },
    "effect": "penalty",
    "weight": 25,
    "reason_text": "Classic grounded theory relies heavily on rich qualitative text and theoretical coding memos."
  },
  {
    "id": "RULE_DATA_TEXT_INTERVIEW_BOOST",
    "method_id": "semi_structured_interview",
    "conditions": {
      "data_type": "textual_narrative"
    },
    "effect": "boost",
    "weight": 30,
    "reason_text": "Semi-structured interviews excel at eliciting nuanced, open-ended textual narratives from participants."
  },
  {
    "id": "RULE_DATA_TEXT_FOCUS_BOOST",
    "method_id": "focus_group",
    "conditions": {
      "data_type": "textual_narrative"
    },
    "effect": "boost",
    "weight": 25,
    "reason_text": "Focus group discussions generate dynamic collaborative textual transcripts and debate."
  },
  {
    "id": "RULE_DATA_TEXT_EXP_PENALTY",
    "method_id": "experiment",
    "conditions": {
      "data_type": "textual_narrative"
    },
    "effect": "penalty",
    "weight": 35,
    "reason_text": "True experiments require quantitative dependent variables rather than unstructured narrative text."
  },
  {
    "id": "RULE_DATA_BOTH_MIXED_BOOST",
    "method_id": "mixed_methods",
    "conditions": {
      "data_type": "both"
    },
    "effect": "boost",
    "weight": 40,
    "reason_text": "Collecting both numerical metrics and qualitative narratives is the foundation of Mixed Methods research."
  },
  {
    "id": "RULE_DATA_BOTH_ACTION_BOOST",
    "method_id": "action_research",
    "conditions": {
      "data_type": "both"
    },
    "effect": "boost",
    "weight": 25,
    "reason_text": "Action research frequently triangulates quantitative operational metrics with qualitative practitioner reflection."
  },
  {
    "id": "RULE_CTRL_FULL_EXP_BOOST",
    "method_id": "experiment",
    "conditions": {
      "control_over_variables": "full"
    },
    "effect": "boost",
    "weight": 35,
    "reason_text": "Full control over extraneous variables enables randomized laboratory experimentation."
  },
  {
    "id": "RULE_CTRL_NONE_EXP_EXCLUDE",
    "method_id": "experiment",
    "conditions": {
      "control_over_variables": "none"
    },
    "effect": "hard_exclude",
    "weight": 100,
    "reason_text": "True experimental design cannot be conducted without the ability to manipulate and control experimental conditions."
  },
  {
    "id": "RULE_CTRL_NONE_OBS_BOOST",
    "method_id": "observational_study",
    "conditions": {
      "control_over_variables": "none"
    },
    "effect": "boost",
    "weight": 30,
    "reason_text": "Naturalistic observational studies capture behavior in authentic environments without artificial experimental control."
  },
  {
    "id": "RULE_CTRL_NONE_CORR_BOOST",
    "method_id": "correlational_study",
    "conditions": {
      "control_over_variables": "none"
    },
    "effect": "boost",
    "weight": 25,
    "reason_text": "Correlational studies observe natural covariation between variables without intervention or manipulation."
  },
  {
    "id": "RULE_CTRL_PARTIAL_QUASI_BOOST",
    "method_id": "quasi_experiment",
    "conditions": {
      "control_over_variables": "partial"
    },
    "effect": "boost",
    "weight": 30,
    "reason_text": "Quasi-experimental designs are tailored for situations where only partial control over treatment allocation is possible."
  },
  {
    "id": "RULE_SAMPLE_SMALL_SURVEY_EXCLUDE",
    "method_id": "survey",
    "conditions": {
      "sample_size_available": "under_10"
    },
    "effect": "hard_exclude",
    "weight": 100,
    "reason_text": "A sample size of fewer than 10 participants lacks sufficient statistical power for survey research."
  },
  {
    "id": "RULE_SAMPLE_SMALL_META_EXCLUDE",
    "method_id": "meta_analysis",
    "conditions": {
      "sample_size_available": "under_10"
    },
    "effect": "hard_exclude",
    "weight": 100,
    "reason_text": "Meta-analysis requires statistical pooling across dozens of primary studies and cannot operate on a sample of under 10."
  },
  {
    "id": "RULE_SAMPLE_SMALL_CASE_BOOST",
    "method_id": "case_study",
    "conditions": {
      "sample_size_available": "under_10"
    },
    "effect": "boost",
    "weight": 30,
    "reason_text": "Case study research is optimized for small, bounded samples (1-5 units) analyzed in extreme depth."
  },
  {
    "id": "RULE_SAMPLE_SMALL_PHENOM_BOOST",
    "method_id": "phenomenology",
    "conditions": {
      "sample_size_available": "under_10"
    },
    "effect": "boost",
    "weight": 30,
    "reason_text": "Phenomenological inquiries intentionally use small, targeted samples (5-10 individuals) to distill universal essences."
  },
  {
    "id": "RULE_SAMPLE_LARGE_SURVEY_BOOST",
    "method_id": "survey",
    "conditions": {
      "sample_size_available": "over_100"
    },
    "effect": "boost",
    "weight": 30,
    "reason_text": "A large sample (>100) provides the statistical power needed for robust survey generalizations and regression."
  },
  {
    "id": "RULE_SAMPLE_LARGE_CORR_BOOST",
    "method_id": "correlational_study",
    "conditions": {
      "sample_size_available": "over_100"
    },
    "effect": "boost",
    "weight": 25,
    "reason_text": "Ample sample size enables multivariate regression and structural equation modeling."
  },
  {
    "id": "RULE_SAMPLE_MID_INTERVIEW_BOOST",
    "method_id": "semi_structured_interview",
    "conditions": {
      "sample_size_available": "10_to_30"
    },
    "effect": "boost",
    "weight": 25,
    "reason_text": "A sample of 10 to 30 participants is the sweet spot for achieving qualitative saturation in semi-structured interviews."
  },
  {
    "id": "RULE_TIME_SHORT_LONGITUDINAL_EXCLUDE",
    "method_id": "longitudinal_study",
    "conditions": {
      "time_available": "under_1_month"
    },
    "effect": "hard_exclude",
    "weight": 100,
    "reason_text": "A longitudinal study requires tracking temporal trajectories over months or years; it cannot be completed in under 1 month."
  },
  {
    "id": "RULE_TIME_SHORT_ETHNO_EXCLUDE",
    "method_id": "ethnography",
    "conditions": {
      "time_available": "under_1_month"
    },
    "effect": "hard_exclude",
    "weight": 100,
    "reason_text": "Meaningful ethnographic immersion requires sustained field presence and cannot be accomplished in less than a month."
  },
  {
    "id": "RULE_TIME_SHORT_CROSS_SECT_BOOST",
    "method_id": "cross_sectional_study",
    "conditions": {
      "time_available": "under_1_month"
    },
    "effect": "boost",
    "weight": 30,
    "reason_text": "Cross-sectional point-in-time studies are well-suited for rapid completion under tight academic deadlines."
  },
  {
    "id": "RULE_TIME_SHORT_CONTENT_BOOST",
    "method_id": "content_analysis",
    "conditions": {
      "time_available": "under_1_month"
    },
    "effect": "boost",
    "weight": 25,
    "reason_text": "Content analysis of existing online or archival texts can be executed rapidly without scheduling human participant interviews."
  },
  {
    "id": "RULE_TIME_LONG_LONGITUDINAL_BOOST",
    "method_id": "longitudinal_study",
    "conditions": {
      "time_available": "over_6_months"
    },
    "effect": "boost",
    "weight": 35,
    "reason_text": "A timeframe exceeding 6 months makes a multi-wave longitudinal panel study feasible."
  },
  {
    "id": "RULE_TIME_LONG_ETHNO_BOOST",
    "method_id": "ethnography",
    "conditions": {
      "time_available": "over_6_months"
    },
    "effect": "boost",
    "weight": 30,
    "reason_text": "Extended calendar availability permits the sustained cultural field immersion that characterizes exemplary ethnography."
  },
  {
    "id": "RULE_ACCESS_NONE_FIELD_EXCLUDE_INTERVIEW",
    "method_id": "semi_structured_interview",
    "conditions": {
      "participant_access": "none_secondary_only"
    },
    "effect": "hard_exclude",
    "weight": 100,
    "reason_text": "Interviews require direct access to human informants and cannot be conducted with secondary data alone."
  },
  {
    "id": "RULE_ACCESS_NONE_FIELD_EXCLUDE_FOCUS",
    "method_id": "focus_group",
    "conditions": {
      "participant_access": "none_secondary_only"
    },
    "effect": "hard_exclude",
    "weight": 100,
    "reason_text": "Focus group discussions require in-person or live virtual group interactions with human participants."
  },
  {
    "id": "RULE_ACCESS_NONE_FIELD_EXCLUDE_EXP",
    "method_id": "experiment",
    "conditions": {
      "participant_access": "none_secondary_only"
    },
    "effect": "hard_exclude",
    "weight": 100,
    "reason_text": "Experimental human testing requires direct access to study subjects for intervention trials."
  },
  {
    "id": "RULE_ACCESS_NONE_SLR_BOOST",
    "method_id": "systematic_literature_review",
    "conditions": {
      "participant_access": "none_secondary_only"
    },
    "effect": "boost",
    "weight": 40,
    "reason_text": "When human participants are unavailable, synthesizing the existing empirical literature via SLR is ideal."
  },
  {
    "id": "RULE_ACCESS_NONE_META_BOOST",
    "method_id": "meta_analysis",
    "conditions": {
      "participant_access": "none_secondary_only"
    },
    "effect": "boost",
    "weight": 35,
    "reason_text": "Meta-analysis operates entirely on published quantitative secondary literature without requiring participant recruitment."
  },
  {
    "id": "RULE_ACCESS_NONE_CONTENT_BOOST",
    "method_id": "content_analysis",
    "conditions": {
      "participant_access": "none_secondary_only"
    },
    "effect": "boost",
    "weight": 35,
    "reason_text": "Content analysis of existing public documents or digital archives does not require participant recruitment."
  },
  {
    "id": "RULE_THEORY_NONE_GT_BOOST",
    "method_id": "grounded_theory",
    "conditions": {
      "existing_theory": "none"
    },
    "effect": "boost",
    "weight": 40,
    "reason_text": "When theoretical explanations are lacking, Grounded Theory is the method of choice to construct an inductive theory."
  },
  {
    "id": "RULE_THEORY_ESTABLISHED_EXP_BOOST",
    "method_id": "experiment",
    "conditions": {
      "existing_theory": "well_established"
    },
    "effect": "boost",
    "weight": 25,
    "reason_text": "Well-established theories provide the precise deductive hypotheses needed for controlled experimental tests."
  },
  {
    "id": "RULE_THEORY_ESTABLISHED_CORR_BOOST",
    "method_id": "correlational_study",
    "conditions": {
      "existing_theory": "well_established"
    },
    "effect": "boost",
    "weight": 20,
    "reason_text": "Mature theoretical models supply validated constructs and measurement instruments for quantitative correlation."
  },
  {
    "id": "RULE_THEORY_ESTABLISHED_GT_PENALTY",
    "method_id": "grounded_theory",
    "conditions": {
      "existing_theory": "well_established"
    },
    "effect": "penalty",
    "weight": 25,
    "reason_text": "Classic grounded theory is designed for theoretical discovery; testing established theories is better suited to deductive designs."
  },
  {
    "id": "RULE_TIMEFRAME_ONETIME_LONGITUDINAL_EXCLUDE",
    "method_id": "longitudinal_study",
    "conditions": {
      "study_timeframe": "one_time"
    },
    "effect": "hard_exclude",
    "weight": 100,
    "reason_text": "A one-time cross-sectional snapshot is conceptually incompatible with a longitudinal study design."
  },
  {
    "id": "RULE_TIMEFRAME_ONETIME_CROSS_BOOST",
    "method_id": "cross_sectional_study",
    "conditions": {
      "study_timeframe": "one_time"
    },
    "effect": "boost",
    "weight": 35,
    "reason_text": "Cross-sectional research is designed specifically for point-in-time observational investigations."
  },
  {
    "id": "RULE_TIMEFRAME_OVERTIME_LONGITUDINAL_BOOST",
    "method_id": "longitudinal_study",
    "conditions": {
      "study_timeframe": "over_time"
    },
    "effect": "boost",
    "weight": 40,
    "reason_text": "Tracking phenomena over multiple chronological points directly fulfills the longitudinal methodology."
  },
  {
    "id": "RULE_TIMEFRAME_OVERTIME_ACTION_BOOST",
    "method_id": "action_research",
    "conditions": {
      "study_timeframe": "over_time"
    },
    "effect": "boost",
    "weight": 30,
    "reason_text": "Action research thrives across iterative temporal cycles of planning, executing, and evaluating over time."
  },
  {
    "id": "RULE_ETHICS_HIGH_INTERVENTION_PENALTY",
    "method_id": "experiment",
    "conditions": {
      "ethical_sensitivity": "high"
    },
    "effect": "penalty",
    "weight": 20,
    "reason_text": "High ethical vulnerability poses institutional review challenges when subjecting participants to experimental interventions."
  },
  {
    "id": "RULE_ETHICS_HIGH_SECONDARY_BOOST",
    "method_id": "systematic_literature_review",
    "conditions": {
      "ethical_sensitivity": "high"
    },
    "effect": "boost",
    "weight": 20,
    "reason_text": "Secondary literature synthesis mitigates risks of causing direct harm to vulnerable research subjects."
  },
  {
    "id": "RULE_DOMAIN_ENG_DSR_BOOST",
    "method_id": "design_science_research",
    "conditions": {
      "domain": "engineering"
    },
    "effect": "boost",
    "weight": 25,
    "reason_text": "Engineering projects strongly favor artifact creation and technical prototype evaluation (Design Science Research)."
  },
  {
    "id": "RULE_DOMAIN_MGMT_CASE_BOOST",
    "method_id": "case_study",
    "conditions": {
      "domain": "management"
    },
    "effect": "boost",
    "weight": 20,
    "reason_text": "Management research frequently utilizes organizational case studies to investigate leadership and strategy in context."
  },
  {
    "id": "RULE_DOMAIN_EDU_ACTION_BOOST",
    "method_id": "action_research",
    "conditions": {
      "domain": "education"
    },
    "effect": "boost",
    "weight": 25,
    "reason_text": "Educational research benefits extensively from classroom-based action research conducted by teacher-practitioners."
  },
  {
    "id": "RULE_DOMAIN_HEALTH_EXP_BOOST",
    "method_id": "experiment",
    "conditions": {
      "domain": "health"
    },
    "effect": "boost",
    "weight": 25,
    "reason_text": "Health and medical sciences view randomized controlled experimental trials as the gold standard for evidence."
  }
];
const BENCHMARKS_DATA = [
  {
    "scenario_id": "BENCH_01",
    "title": "Evaluating a Low-Latency Consensus Algorithm for Edge Computing",
    "domain": "engineering",
    "description": "Designing, building, and benchmarking a novel consensus algorithm across simulated IoT sensor networks to measure throughput and latency.",
    "questionnaire_inputs": {
      "research_objective": "build_evaluate_artifact",
      "data_type": "numerical",
      "control_over_variables": "full",
      "sample_size_available": "30_to_100",
      "time_available": "3_to_6_months",
      "budget": "medium",
      "participant_access": "easy",
      "existing_theory": "well_established",
      "study_timeframe": "one_time",
      "domain": "engineering",
      "ethical_sensitivity": "low"
    },
    "expected_method_ids": [
      "design_science_research",
      "experiment"
    ],
    "rationale": "Creating and evaluating a novel software artifact requires Design Science Research paired with controlled algorithmic benchmarking.",
    "faculty_contributor": "Dr. K. Raman (Computer Engineering)"
  },
  {
    "scenario_id": "BENCH_02",
    "title": "Survey of Hybrid Work Adoption Across IT Enterprises",
    "domain": "management",
    "description": "Administering a validated Likert questionnaire to 300 software engineers across 15 IT firms to describe satisfaction and turnover intention.",
    "questionnaire_inputs": {
      "research_objective": "describe",
      "data_type": "numerical",
      "control_over_variables": "none",
      "sample_size_available": "over_100",
      "time_available": "1_to_3_months",
      "budget": "low",
      "participant_access": "easy",
      "existing_theory": "well_established",
      "study_timeframe": "one_time",
      "domain": "management",
      "ethical_sensitivity": "low"
    },
    "expected_method_ids": [
      "survey",
      "cross_sectional_study"
    ],
    "rationale": "Large-scale descriptive point-in-time profiling with numerical Likert scales is the classic domain of survey research.",
    "faculty_contributor": "Prof. E. Martinez (Organizational Behavior)"
  },
  {
    "scenario_id": "BENCH_03",
    "title": "Exploring Lived Experiences of ICU Burnout During Pandemic Surges",
    "domain": "health",
    "description": "Conducting in-depth open interviews with 12 senior ICU nurses to understand the subjective emotional essence of prolonged trauma.",
    "questionnaire_inputs": {
      "research_objective": "explore",
      "data_type": "textual_narrative",
      "control_over_variables": "none",
      "sample_size_available": "10_to_30",
      "time_available": "3_to_6_months",
      "budget": "low",
      "participant_access": "easy",
      "existing_theory": "none",
      "study_timeframe": "one_time",
      "domain": "health",
      "ethical_sensitivity": "high"
    },
    "expected_method_ids": [
      "phenomenology",
      "semi_structured_interview",
      "grounded_theory"
    ],
    "rationale": "Uncovering the lived essence of deeply affective personal human trauma requires phenomenological inquiry or in-depth interviews.",
    "faculty_contributor": "Dr. L. Chen (Clinical Nursing)"
  },
  {
    "scenario_id": "BENCH_04",
    "title": "In-Depth Study of Agile Transformation Resistance in a Banking Giant",
    "domain": "management",
    "description": "Investigating the holistic socio-technical resistance factors during a 9-month cloud transformation inside a legacy multinational bank.",
    "questionnaire_inputs": {
      "research_objective": "explore",
      "data_type": "both",
      "control_over_variables": "partial",
      "sample_size_available": "10_to_30",
      "time_available": "over_6_months",
      "budget": "medium",
      "participant_access": "easy",
      "existing_theory": "limited",
      "study_timeframe": "over_time",
      "domain": "management",
      "ethical_sensitivity": "medium"
    },
    "expected_method_ids": [
      "case_study",
      "action_research"
    ],
    "rationale": "Holistic, context-dependent investigation within a single organizational boundary across months requires Case Study research.",
    "faculty_contributor": "Prof. H. Tanaka (Enterprise Systems)"
  },
  {
    "scenario_id": "BENCH_05",
    "title": "Systematic Review of Static Security Analysis in DevSecOps",
    "domain": "engineering",
    "description": "Retrieving, screening, and synthesizing 70 published peer-reviewed studies following the PRISMA protocol to assess static vulnerability detection accuracy.",
    "questionnaire_inputs": {
      "research_objective": "review_literature",
      "data_type": "both",
      "control_over_variables": "none",
      "sample_size_available": "30_to_100",
      "time_available": "3_to_6_months",
      "budget": "low",
      "participant_access": "none_secondary_only",
      "existing_theory": "well_established",
      "study_timeframe": "one_time",
      "domain": "engineering",
      "ethical_sensitivity": "low"
    },
    "expected_method_ids": [
      "systematic_literature_review"
    ],
    "rationale": "Synthesizing secondary published empirical studies without human participants is the domain of Systematic Literature Review.",
    "faculty_contributor": "Dr. A. Vance (Software Engineering)"
  },
  {
    "scenario_id": "BENCH_06",
    "title": "Meta-Analysis of High-Intensity Interval Training on Cardiovascular Biomarkers",
    "domain": "health",
    "description": "Extracting effect sizes (Hedges' g) from 35 randomized trials to calculate the pooled effect of HIIT on arterial stiffness.",
    "questionnaire_inputs": {
      "research_objective": "review_literature",
      "data_type": "numerical",
      "control_over_variables": "none",
      "sample_size_available": "30_to_100",
      "time_available": "3_to_6_months",
      "budget": "low",
      "participant_access": "none_secondary_only",
      "existing_theory": "well_established",
      "study_timeframe": "one_time",
      "domain": "health",
      "ethical_sensitivity": "low"
    },
    "expected_method_ids": [
      "meta_analysis",
      "systematic_literature_review"
    ],
    "rationale": "Quantitative pooling of numerical effect sizes across published clinical trials is Meta-Analysis.",
    "faculty_contributor": "Dr. M. Brooks (Cardiology)"
  },
  {
    "scenario_id": "BENCH_07",
    "title": "Improving Coding Retention Through Peer Instruction Cycles in Secondary CS",
    "domain": "education",
    "description": "A computer science educator runs three consecutive 4-week iterative teaching interventions in their own classroom to resolve syntax misconceptions.",
    "questionnaire_inputs": {
      "research_objective": "evaluate_intervention",
      "data_type": "both",
      "control_over_variables": "partial",
      "sample_size_available": "30_to_100",
      "time_available": "3_to_6_months",
      "budget": "low",
      "participant_access": "easy",
      "existing_theory": "limited",
      "study_timeframe": "over_time",
      "domain": "education",
      "ethical_sensitivity": "low"
    },
    "expected_method_ids": [
      "action_research",
      "quasi_experiment"
    ],
    "rationale": "Practitioner-led iterative problem-solving inside one's own classroom represents textbook Action Research.",
    "faculty_contributor": "Dr. B. Taylor (Educational Inquiry)"
  },
  {
    "scenario_id": "BENCH_08",
    "title": "Controlled Laboratory Trial of IDE Dark Mode on Developer Bug Detection",
    "domain": "engineering",
    "description": "Randomly assigning 60 programmers into treatment (dark mode) and control (light mode) groups to measure syntax error detection latency.",
    "questionnaire_inputs": {
      "research_objective": "explain_test_hypothesis",
      "data_type": "numerical",
      "control_over_variables": "full",
      "sample_size_available": "30_to_100",
      "time_available": "1_to_3_months",
      "budget": "medium",
      "participant_access": "easy",
      "existing_theory": "well_established",
      "study_timeframe": "one_time",
      "domain": "engineering",
      "ethical_sensitivity": "low"
    },
    "expected_method_ids": [
      "experiment"
    ],
    "rationale": "Random assignment with full control over independent variables and numerical latency metrics is a True Experiment.",
    "faculty_contributor": "Dr. K. Raman (Computer Engineering)"
  },
  {
    "scenario_id": "BENCH_09",
    "title": "Quasi-Experimental Evaluation of a Flipped Classroom in Engineering Math",
    "domain": "education",
    "description": "Comparing midterm exam results between Section A (flipped lecture) and Section B (standard lecture) without disrupting student registrations.",
    "questionnaire_inputs": {
      "research_objective": "evaluate_intervention",
      "data_type": "numerical",
      "control_over_variables": "partial",
      "sample_size_available": "30_to_100",
      "time_available": "1_to_3_months",
      "budget": "low",
      "participant_access": "easy",
      "existing_theory": "well_established",
      "study_timeframe": "one_time",
      "domain": "education",
      "ethical_sensitivity": "low"
    },
    "expected_method_ids": [
      "quasi_experiment",
      "action_research"
    ],
    "rationale": "Testing an intervention on intact classrooms without random assignment is a Quasi-Experimental Design.",
    "faculty_contributor": "Dr. B. Taylor (Educational Inquiry)"
  },
  {
    "scenario_id": "BENCH_10",
    "title": "Developing a Grounded Theory of Decision Pivoting in Early-Stage Startups",
    "domain": "management",
    "description": "Conducting iterative open and axial coding interviews with 26 startup founders to build an inductive conceptual model of pivoting phases.",
    "questionnaire_inputs": {
      "research_objective": "explore",
      "data_type": "textual_narrative",
      "control_over_variables": "none",
      "sample_size_available": "10_to_30",
      "time_available": "over_6_months",
      "budget": "low",
      "participant_access": "easy",
      "existing_theory": "none",
      "study_timeframe": "over_time",
      "domain": "management",
      "ethical_sensitivity": "low"
    },
    "expected_method_ids": [
      "grounded_theory",
      "semi_structured_interview"
    ],
    "rationale": "Inductively constructing a substantive theory from participant narratives where no prior theory exists is Grounded Theory.",
    "faculty_contributor": "Prof. E. Martinez (Organizational Behavior)"
  },
  {
    "scenario_id": "BENCH_11",
    "title": "Predicting Student Drop-Out from Virtual Learning Environment Logins",
    "domain": "education",
    "description": "Using linear and logistic regression on 400 student system log files to identify statistical correlation between engagement frequency and drop-out.",
    "questionnaire_inputs": {
      "research_objective": "predict",
      "data_type": "numerical",
      "control_over_variables": "none",
      "sample_size_available": "over_100",
      "time_available": "1_to_3_months",
      "budget": "low",
      "participant_access": "easy",
      "existing_theory": "well_established",
      "study_timeframe": "one_time",
      "domain": "education",
      "ethical_sensitivity": "low"
    },
    "expected_method_ids": [
      "correlational_study",
      "survey"
    ],
    "rationale": "Non-experimental statistical modeling of natural associations to predict an outcome is Correlational Research.",
    "faculty_contributor": "Dr. B. Taylor (Educational Inquiry)"
  },
  {
    "scenario_id": "BENCH_12",
    "title": "Content Analysis of Greenwashing Claims in Fortune 500 Sustainability Reports",
    "domain": "management",
    "description": "Coding 120 corporate sustainability PDF disclosures to categorize linguistic exaggeration vs. auditable carbon emission metrics.",
    "questionnaire_inputs": {
      "research_objective": "describe",
      "data_type": "both",
      "control_over_variables": "none",
      "sample_size_available": "over_100",
      "time_available": "1_to_3_months",
      "budget": "low",
      "participant_access": "none_secondary_only",
      "existing_theory": "limited",
      "study_timeframe": "one_time",
      "domain": "management",
      "ethical_sensitivity": "low"
    },
    "expected_method_ids": [
      "content_analysis",
      "systematic_literature_review"
    ],
    "rationale": "Analyzing documented texts and communication artifacts without human contact is Content Analysis.",
    "faculty_contributor": "Prof. H. Tanaka (Enterprise Systems)"
  },
  {
    "scenario_id": "BENCH_13",
    "title": "Multi-Round Delphi Consensus on Core Competencies for Quantum Software Engineers",
    "domain": "engineering",
    "description": "Engaging 22 international quantum computing researchers through three rounds of anonymous questionnaires to establish curriculum guidelines.",
    "questionnaire_inputs": {
      "research_objective": "explore",
      "data_type": "both",
      "control_over_variables": "none",
      "sample_size_available": "10_to_30",
      "time_available": "3_to_6_months",
      "budget": "low",
      "participant_access": "difficult",
      "existing_theory": "limited",
      "study_timeframe": "over_time",
      "domain": "engineering",
      "ethical_sensitivity": "low"
    },
    "expected_method_ids": [
      "delphi_technique"
    ],
    "rationale": "Reaching consensus among geographically dispersed experts through iterative anonymous questionnaires is the Delphi Technique.",
    "faculty_contributor": "Dr. A. Vance (Software Engineering)"
  },
  {
    "scenario_id": "BENCH_14",
    "title": "Ethnographic Study of On-Call Incident Triage in Distributed DevOps Squads",
    "domain": "engineering",
    "description": "Spending 6 months shadowing and observing software engineering teams during late-night incident triage to uncover implicit workplace norms.",
    "questionnaire_inputs": {
      "research_objective": "explore",
      "data_type": "textual_narrative",
      "control_over_variables": "none",
      "sample_size_available": "10_to_30",
      "time_available": "over_6_months",
      "budget": "medium",
      "participant_access": "easy",
      "existing_theory": "limited",
      "study_timeframe": "over_time",
      "domain": "engineering",
      "ethical_sensitivity": "medium"
    },
    "expected_method_ids": [
      "ethnography",
      "case_study"
    ],
    "rationale": "Prolonged immersion to understand implicit cultural behaviors from an insider perspective is Ethnography.",
    "faculty_contributor": "Dr. A. Vance (Software Engineering)"
  },
  {
    "scenario_id": "BENCH_15",
    "title": "Three-Year Longitudinal Cohort Tracking Cognitive Decline in Aging Adults",
    "domain": "health",
    "description": "Tracking biometric wearables and cognitive battery assessments in 200 seniors at 6-month intervals over 3 years.",
    "questionnaire_inputs": {
      "research_objective": "predict",
      "data_type": "numerical",
      "control_over_variables": "none",
      "sample_size_available": "over_100",
      "time_available": "over_6_months",
      "budget": "high",
      "participant_access": "easy",
      "existing_theory": "well_established",
      "study_timeframe": "over_time",
      "domain": "health",
      "ethical_sensitivity": "medium"
    },
    "expected_method_ids": [
      "longitudinal_study"
    ],
    "rationale": "Repeated measurements on the same cohort across extended time to establish developmental trajectories is a Longitudinal Study.",
    "faculty_contributor": "Dr. M. Brooks (Cardiology)"
  },
  {
    "scenario_id": "BENCH_16",
    "title": "Convergent Mixed Methods on Remote VR Laboratory Efficacy in Physics",
    "domain": "education",
    "description": "Administering pre/post physics tests to 150 students while conducting concurrent qualitative interviews with 20 students to explain outcomes.",
    "questionnaire_inputs": {
      "research_objective": "evaluate_intervention",
      "data_type": "both",
      "control_over_variables": "partial",
      "sample_size_available": "over_100",
      "time_available": "3_to_6_months",
      "budget": "medium",
      "participant_access": "easy",
      "existing_theory": "well_established",
      "study_timeframe": "one_time",
      "domain": "education",
      "ethical_sensitivity": "low"
    },
    "expected_method_ids": [
      "mixed_methods",
      "action_research"
    ],
    "rationale": "Directly integrating both quantitative test metrics and qualitative explanatory interviews is Mixed Methods.",
    "faculty_contributor": "Dr. B. Taylor (Educational Inquiry)"
  },
  {
    "scenario_id": "BENCH_17",
    "title": "Observing Collaborative Social Interaction in Kindergarten STEM Play",
    "domain": "education",
    "description": "Systematically coding video logs of peer turn-taking and physical block sharing among 30 children without researcher intervention.",
    "questionnaire_inputs": {
      "research_objective": "describe",
      "data_type": "textual_narrative",
      "control_over_variables": "none",
      "sample_size_available": "30_to_100",
      "time_available": "1_to_3_months",
      "budget": "low",
      "participant_access": "easy",
      "existing_theory": "limited",
      "study_timeframe": "one_time",
      "domain": "education",
      "ethical_sensitivity": "medium"
    },
    "expected_method_ids": [
      "observational_study",
      "case_study"
    ],
    "rationale": "Systematically recording authentic real-time behaviors without intervention or self-report surveys is an Observational Study.",
    "faculty_contributor": "Dr. B. Taylor (Educational Inquiry)"
  },
  {
    "scenario_id": "BENCH_18",
    "title": "Focus Groups on Public Acceptance of Autonomous AI Medical Diagnosis",
    "domain": "health",
    "description": "Moderating 4 interactive group discussions with 8 patients each to uncover collective emotional debates surrounding algorithmic medical care.",
    "questionnaire_inputs": {
      "research_objective": "explore",
      "data_type": "textual_narrative",
      "control_over_variables": "none",
      "sample_size_available": "30_to_100",
      "time_available": "1_to_3_months",
      "budget": "medium",
      "participant_access": "easy",
      "existing_theory": "limited",
      "study_timeframe": "one_time",
      "domain": "health",
      "ethical_sensitivity": "medium"
    },
    "expected_method_ids": [
      "focus_group",
      "semi_structured_interview"
    ],
    "rationale": "Leveraging group synergy and interpersonal debates to elicit shared societal attitudes is Focus Group inquiry.",
    "faculty_contributor": "Dr. L. Chen (Clinical Nursing)"
  },
  {
    "scenario_id": "BENCH_19",
    "title": "Cross-Sectional Point Prevalence of Ergonomic Pain in Programmers",
    "domain": "health",
    "description": "A one-time digital questionnaire distributed to 250 software engineers across 5 tech hubs during March to assess RSI prevalence.",
    "questionnaire_inputs": {
      "research_objective": "describe",
      "data_type": "numerical",
      "control_over_variables": "none",
      "sample_size_available": "over_100",
      "time_available": "under_1_month",
      "budget": "low",
      "participant_access": "easy",
      "existing_theory": "well_established",
      "study_timeframe": "one_time",
      "domain": "health",
      "ethical_sensitivity": "low"
    },
    "expected_method_ids": [
      "cross_sectional_study",
      "survey"
    ],
    "rationale": "Rapid point-in-time observational survey assessing prevalence across an occupational group is Cross-Sectional Study.",
    "faculty_contributor": "Dr. M. Brooks (Cardiology)"
  },
  {
    "scenario_id": "BENCH_20",
    "title": "Design and Benchmark Evaluation of an ML Anomaly Detector for SCADA",
    "domain": "engineering",
    "description": "Constructing an ensemble autoencoder artifact and evaluating false-positive rates against benchmark industrial control datasets.",
    "questionnaire_inputs": {
      "research_objective": "build_evaluate_artifact",
      "data_type": "numerical",
      "control_over_variables": "full",
      "sample_size_available": "30_to_100",
      "time_available": "3_to_6_months",
      "budget": "low",
      "participant_access": "easy",
      "existing_theory": "limited",
      "study_timeframe": "one_time",
      "domain": "engineering",
      "ethical_sensitivity": "low"
    },
    "expected_method_ids": [
      "design_science_research",
      "experiment"
    ],
    "rationale": "Developing novel algorithmic software solutions and benchmarking performance follows Design Science Research.",
    "faculty_contributor": "Dr. K. Raman (Computer Engineering)"
  },
  {
    "scenario_id": "BENCH_21",
    "title": "Semi-Structured Interviews on CISO Trade-Offs in Cloud Migration",
    "domain": "management",
    "description": "Interviewing 16 Chief Information Security Officers to explore unwritten organizational barriers to corporate cloud governance.",
    "questionnaire_inputs": {
      "research_objective": "explore",
      "data_type": "textual_narrative",
      "control_over_variables": "none",
      "sample_size_available": "10_to_30",
      "time_available": "1_to_3_months",
      "budget": "low",
      "participant_access": "easy",
      "existing_theory": "limited",
      "study_timeframe": "one_time",
      "domain": "management",
      "ethical_sensitivity": "low"
    },
    "expected_method_ids": [
      "semi_structured_interview",
      "case_study"
    ],
    "rationale": "Targeted in-depth conversations with 10-30 subject matter experts to elicit qualitative insights represents Semi-Structured Interviews.",
    "faculty_contributor": "Prof. E. Martinez (Organizational Behavior)"
  },
  {
    "scenario_id": "BENCH_22",
    "title": "Double-Blind Drug Trial on Hypertension Reduction in Type-2 Diabetics",
    "domain": "health",
    "description": "Randomized double-blind placebo-controlled clinical trial with 80 patients measuring diastolic blood pressure over 8 weeks.",
    "questionnaire_inputs": {
      "research_objective": "explain_test_hypothesis",
      "data_type": "numerical",
      "control_over_variables": "full",
      "sample_size_available": "30_to_100",
      "time_available": "3_to_6_months",
      "budget": "high",
      "participant_access": "easy",
      "existing_theory": "well_established",
      "study_timeframe": "one_time",
      "domain": "health",
      "ethical_sensitivity": "high"
    },
    "expected_method_ids": [
      "experiment"
    ],
    "rationale": "Randomized clinical trials testing causal physiological treatment effects are True Experiments.",
    "faculty_contributor": "Dr. M. Brooks (Cardiology)"
  },
  {
    "scenario_id": "BENCH_23",
    "title": "Synthesizing 50 Studies on Microfinance Impact in South Asia",
    "domain": "social_science",
    "description": "Systematic literature review following PRISMA guidelines evaluating rural household income outcomes from 50 peer-reviewed papers.",
    "questionnaire_inputs": {
      "research_objective": "review_literature",
      "data_type": "both",
      "control_over_variables": "none",
      "sample_size_available": "30_to_100",
      "time_available": "3_to_6_months",
      "budget": "low",
      "participant_access": "none_secondary_only",
      "existing_theory": "well_established",
      "study_timeframe": "one_time",
      "domain": "social_science",
      "ethical_sensitivity": "low"
    },
    "expected_method_ids": [
      "systematic_literature_review"
    ],
    "rationale": "Comprehensive, protocol-driven secondary synthesis of empirical papers is Systematic Literature Review.",
    "faculty_contributor": "Prof. S. Jenkins (Research Methodology)"
  },
  {
    "scenario_id": "BENCH_24",
    "title": "Action Research on Clinical Handover Protocols in a Rural Emergency Ward",
    "domain": "health",
    "description": "Emergency room physicians and nurses work collaboratively in three cycles to refine a computerized patient handover checklist.",
    "questionnaire_inputs": {
      "research_objective": "evaluate_intervention",
      "data_type": "both",
      "control_over_variables": "partial",
      "sample_size_available": "10_to_30",
      "time_available": "3_to_6_months",
      "budget": "low",
      "participant_access": "easy",
      "existing_theory": "limited",
      "study_timeframe": "over_time",
      "domain": "health",
      "ethical_sensitivity": "medium"
    },
    "expected_method_ids": [
      "action_research"
    ],
    "rationale": "Healthcare practitioners actively refining their own operational procedures in iterative cycles is Action Research.",
    "faculty_contributor": "Dr. L. Chen (Clinical Nursing)"
  },
  {
    "scenario_id": "BENCH_25",
    "title": "Investigating the Lived Experience of Sudden Sensory Loss in Veterans",
    "domain": "social_science",
    "description": "Phenomenological interviews with 9 military veterans to distill the existential and emotional meaning of sudden acoustic trauma.",
    "questionnaire_inputs": {
      "research_objective": "explore",
      "data_type": "textual_narrative",
      "control_over_variables": "none",
      "sample_size_available": "under_10",
      "time_available": "3_to_6_months",
      "budget": "low",
      "participant_access": "difficult",
      "existing_theory": "none",
      "study_timeframe": "one_time",
      "domain": "social_science",
      "ethical_sensitivity": "high"
    },
    "expected_method_ids": [
      "phenomenology",
      "case_study"
    ],
    "rationale": "In-depth emotional inquiry with fewer than 10 individuals to capture the essence of a shared lived experience is Phenomenology.",
    "faculty_contributor": "Prof. S. Jenkins (Research Methodology)"
  },
  {
    "scenario_id": "BENCH_26",
    "title": "Predicting Employee Turnover from Annual Engagement Scores and Commute Times",
    "domain": "management",
    "description": "Multiple linear regression analysis of 350 employee survey records to model how commute length correlates with voluntary attrition.",
    "questionnaire_inputs": {
      "research_objective": "predict",
      "data_type": "numerical",
      "control_over_variables": "none",
      "sample_size_available": "over_100",
      "time_available": "1_to_3_months",
      "budget": "low",
      "participant_access": "easy",
      "existing_theory": "well_established",
      "study_timeframe": "one_time",
      "domain": "management",
      "ethical_sensitivity": "low"
    },
    "expected_method_ids": [
      "correlational_study",
      "survey"
    ],
    "rationale": "Statistical regression modeling to predict outcomes from multiple continuous predictors without manipulation is Correlational Study.",
    "faculty_contributor": "Prof. E. Martinez (Organizational Behavior)"
  },
  {
    "scenario_id": "BENCH_27",
    "title": "Constructing and Evaluating a Microservices Architectural Simulator",
    "domain": "engineering",
    "description": "Implementing an open-source event-driven simulation tool and benchmarking its queue fidelity against production Kubernetes telemetry.",
    "questionnaire_inputs": {
      "research_objective": "build_evaluate_artifact",
      "data_type": "numerical",
      "control_over_variables": "full",
      "sample_size_available": "under_10",
      "time_available": "3_to_6_months",
      "budget": "low",
      "participant_access": "easy",
      "existing_theory": "limited",
      "study_timeframe": "one_time",
      "domain": "engineering",
      "ethical_sensitivity": "low"
    },
    "expected_method_ids": [
      "design_science_research"
    ],
    "rationale": "Constructing a software architecture tool artifact and validating its operational utility is Design Science Research.",
    "faculty_contributor": "Dr. K. Raman (Computer Engineering)"
  },
  {
    "scenario_id": "BENCH_28",
    "title": "Field Observation of Pedestrian Jaywalking Behaviors at Smart Crosswalks",
    "domain": "social_science",
    "description": "Observing and coding 60 hours of video recordings at 4 urban intersections to record pedestrian reaction to countdown timers.",
    "questionnaire_inputs": {
      "research_objective": "describe",
      "data_type": "numerical",
      "control_over_variables": "none",
      "sample_size_available": "over_100",
      "time_available": "1_to_3_months",
      "budget": "low",
      "participant_access": "easy",
      "existing_theory": "limited",
      "study_timeframe": "one_time",
      "domain": "social_science",
      "ethical_sensitivity": "low"
    },
    "expected_method_ids": [
      "observational_study",
      "cross_sectional_study"
    ],
    "rationale": "Systematically observing public behavioral frequencies in real-world settings is an Observational Study.",
    "faculty_contributor": "Prof. S. Jenkins (Research Methodology)"
  },
  {
    "scenario_id": "BENCH_29",
    "title": "Delphi Consensus on Clinical Guidelines for Pediatric Telemedicine",
    "domain": "health",
    "description": "Engaging 24 pediatric chiefs of medicine across 3 feedback iterations to develop national remote triage guidelines.",
    "questionnaire_inputs": {
      "research_objective": "explore",
      "data_type": "both",
      "control_over_variables": "none",
      "sample_size_available": "10_to_30",
      "time_available": "3_to_6_months",
      "budget": "low",
      "participant_access": "difficult",
      "existing_theory": "limited",
      "study_timeframe": "over_time",
      "domain": "health",
      "ethical_sensitivity": "medium"
    },
    "expected_method_ids": [
      "delphi_technique"
    ],
    "rationale": "Developing clinical guidelines via iterative expert consensus rounds is the Delphi Technique.",
    "faculty_contributor": "Dr. L. Chen (Clinical Nursing)"
  },
  {
    "scenario_id": "BENCH_30",
    "title": "Ethnographic Immersion in Rural Traditional Craft Guilds",
    "domain": "social_science",
    "description": "Spending 8 months living alongside traditional handloom weavers to document apprenticeship rituals and cultural language.",
    "questionnaire_inputs": {
      "research_objective": "explore",
      "data_type": "textual_narrative",
      "control_over_variables": "none",
      "sample_size_available": "10_to_30",
      "time_available": "over_6_months",
      "budget": "medium",
      "participant_access": "easy",
      "existing_theory": "none",
      "study_timeframe": "over_time",
      "domain": "social_science",
      "ethical_sensitivity": "medium"
    },
    "expected_method_ids": [
      "ethnography",
      "case_study"
    ],
    "rationale": "Prolonged cultural immersion and participant observation over months is classic Ethnography.",
    "faculty_contributor": "Prof. S. Jenkins (Research Methodology)"
  }
];
