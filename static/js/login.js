function LoginPage() {
  React.useEffect(() => {
    document.body.classList.add("login-bg");
    return () => document.body.classList.remove("login-bg");
  }, []);

  return (
    <div className="container min-vh-100 d-flex align-items-center justify-content-center py-4">
      <div className="card login-card w-100" style={{ maxWidth: "430px" }}>
        <div className="card-body p-4 p-md-5">
          <h1 className="h3 text-center login-title mb-2">Welcome Back</h1>
          <p className="text-center login-subtitle mb-4">
            Sign in to continue to your account.
          </p>

          <form>
            <div className="mb-3">
              <label className="form-label fw-semibold" htmlFor="email">
                Email
              </label>
              <input
                className="form-control login-input"
                id="email"
                type="email"
                placeholder="you@example.com"
              />
            </div>

            <div className="mb-3">
              <label className="form-label fw-semibold" htmlFor="password">
                Password
              </label>
              <input
                className="form-control login-input"
                id="password"
                type="password"
                placeholder="Enter your password"
              />
            </div>

            <div className="d-flex justify-content-between align-items-center mb-4">
              <div className="form-check">
                <input className="form-check-input" type="checkbox" id="rememberMe" />
                <label className="form-check-label" htmlFor="rememberMe">
                  Remember me
                </label>
              </div>
              <a className="forgot-link" href="#">
                Forgot password?
              </a>
            </div>

            <button className="btn btn-primary w-100 py-2 fw-semibold" type="submit">
              Login
            </button>
          </form>

          <p className="text-center text-secondary mt-4 mb-0">
            Don&apos;t have an account? <a href="#">Register</a>
          </p>
        </div>
      </div>
    </div>
  );
}

ReactDOM.createRoot(document.getElementById("root")).render(<LoginPage />);
