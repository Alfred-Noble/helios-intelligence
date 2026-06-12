import {
  getAnalytics,
  getLeads,
  getProjects
} from "../lib/api";

export default async function Home() {
  const analytics = await getAnalytics();

  const leads = await getLeads();

  const projects = await getProjects();

  return (
    <main
      style={{
        padding: "40px",
        maxWidth: "1400px",
        margin: "auto",
        position: "relative",
        zIndex: 1
      }}
    >
      <div className="orb"></div>

      {/* HERO SECTION */}

      <section
        style={{
          textAlign: "center",
          marginBottom: "50px"
        }}
      >
        <h1 className="hero-title">
          ◎ HELIOS
        </h1>

        <h2
          style={{
            fontSize: "30px",
            marginBottom: "15px"
          }}
        >
          Intelligence Platform
        </h2>

        <p
          style={{
            color: "#94a3b8",
            maxWidth: "800px",
            margin: "0 auto",
            lineHeight: "1.8"
          }}
        >
          AI-Powered GTM & Relationship Intelligence Platform
          for Lead Discovery, Persona Classification,
          Outreach Automation and Project-Based Matching.
        </p>
      </section>

      {/* STATS */}

      <section
        style={{
          display: "grid",
          gridTemplateColumns:
            "repeat(auto-fit,minmax(250px,1fr))",
          gap: "20px",
          marginBottom: "30px"
        }}
      >
        <div className="card">
          <div className="stat-number">{analytics.total_leads}</div>
          <h3>Total Leads</h3>
          <p style={{ color: "#94a3b8" }}>
            Imported and analyzed
          </p>
        </div>

        <div className="card">
          <div className="stat-number">
            {Array.isArray(projects) ? projects.length : 0}
          </div>
          <h3>Projects</h3>
          <p style={{ color: "#94a3b8" }}>
            Active GTM campaigns
          </p>
        </div>

        <div className="card">
          <div className="stat-number">{analytics.high_potential}</div>
          <h3>High Potential</h3>
          <p style={{ color: "#94a3b8" }}>
            AI-qualified prospects
          </p>
        </div>

        <div className="card">
          <div className="stat-number">100%</div>
          <h3>Email Delivery</h3>
          <p style={{ color: "#94a3b8" }}>
            SMTP integration active
          </p>
        </div>
      </section>

      {/* FEATURES */}

      <section
        style={{
          display: "grid",
          gridTemplateColumns:
            "repeat(auto-fit,minmax(300px,1fr))",
          gap: "20px"
        }}
      >
        <div className="card">
          <h2>🧠 AI Intelligence</h2>

          <br />

          <ul
            style={{
              lineHeight: "2"
            }}
          >
            <li>Lead Scoring Engine</li>
            <li>Persona Classification</li>
            <li>Project Matching</li>
            <li>GTM Intelligence</li>
          </ul>
        </div>

        <div className="card">
          <h2>⚡ Automation</h2>

          <br />

          <ul
            style={{
              lineHeight: "2"
            }}
          >
            <li>CSV Import</li>
            <li>Email Outreach</li>
            <li>JWT Authentication</li>
            <li>Analytics Dashboard</li>
          </ul>
        </div>

        <div className="card">
          <h2>🚀 Platform Status</h2>

          <br />

          <p>
            Backend APIs Operational
          </p>

          <br />

          <p>
            Database Connected
          </p>

          <br />

          <p>
            SMTP Active
          </p>

          <br />

          <p>
            AI Layer Integrated
          </p>
        </div>
      </section>

      {/* TECH STACK */}

      <div
        className="card"
        style={{
          marginTop: "30px"
        }}
      >
        <h2>⚙ Technology Stack</h2>

        <br />

        <p>
          FastAPI • PostgreSQL • SQLAlchemy
        </p>

        <br />

        <p>
          Next.js • TypeScript • JWT
        </p>

        <br />

        <p>
          SMTP • AI Intelligence Layer • GTM Engine
        </p>
      </div>

      {/* RECENT LEADS */}

      <div
        className="card"
        style={{
          marginTop: "30px"
        }}
      >
        <h2>📊 Recent Leads</h2>

        <br />

        <table
          style={{
            width: "100%",
            borderCollapse: "collapse"
          }}
        >
          <thead>
            <tr>
              <th align="left">Name</th>
              <th align="left">Company</th>
              <th align="left">Industry</th>
            </tr>
          </thead>
          <tbody>
            {Array.isArray(leads.items) &&
              leads.items.slice(0, 5).map(
                (lead: {
                  id: number;
                  full_name: string;
                  company: string;
                  industry: string;
                }) => (
                  <tr key={lead.id}>
                    <td>{lead.full_name}</td>
                    <td>{lead.company}</td>
                    <td>{lead.industry}</td>
                  </tr>
                )
              )}
          </tbody>
        </table>
      </div>

      {/* FOOTER */}

      <div
        style={{
          textAlign: "center",
          marginTop: "40px",
          color: "#94a3b8"
        }}
      >
        Built by Alfred Noble • Final Semester Project 2026
      </div>
    </main>
  );
}