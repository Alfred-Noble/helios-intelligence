export default function Home() {
  return (
    <main
      style={{
        padding: "40px",
        maxWidth: "1400px",
        margin: "auto"
      }}
    >
      <h1
        style={{
          fontSize: "48px",
          marginBottom: "10px"
        }}
      >
        🚀 Helios Intelligence
      </h1>

      <p
        style={{
          color: "#94a3b8",
          marginBottom: "40px"
        }}
      >
        AI-Powered GTM & Relationship Intelligence Platform
      </p>

      <div
        style={{
          display: "grid",
          gridTemplateColumns:
            "repeat(auto-fit,minmax(250px,1fr))",
          gap: "20px"
        }}
      >
        <div className="card">
          <div className="stat-number">10</div>
          <h3>Total Leads</h3>
        </div>

        <div className="card">
          <div className="stat-number">1</div>
          <h3>Projects</h3>
        </div>

        <div className="card">
          <div className="stat-number">1</div>
          <h3>High Potential Leads</h3>
        </div>
      </div>

      <div
        className="card"
        style={{
          marginTop: "30px"
        }}
      >
        <h2>Platform Capabilities</h2>

        <br />

        <ul>
          <li>AI Lead Scoring</li>
          <li>Persona Classification</li>
          <li>Project-Based Matching</li>
          <li>JWT Authentication</li>
          <li>SMTP Email Outreach</li>
          <li>Analytics Dashboard</li>
        </ul>
      </div>

      <div
        className="card"
        style={{
          marginTop: "30px"
        }}
      >
        <h2>Recent Leads</h2>

        <br />

        <table
          style={{
            width: "100%"
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
            <tr>
              <td>Alfred Noble</td>
              <td>KrypC</td>
              <td>Blockchain</td>
            </tr>

            <tr>
              <td>Ananya Gupta</td>
              <td>VisionAI</td>
              <td>Artificial Intelligence</td>
            </tr>

            <tr>
              <td>Rahul Sharma</td>
              <td>FinEdge</td>
              <td>FinTech</td>
            </tr>
          </tbody>
        </table>
      </div>
    </main>
  );
}