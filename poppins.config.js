module.exports = function (poppins) {
  poppins.config = {
    // Github repo to watch
    // https://github.com/myname/myrepo
    target: {
      user: 'henryaspegren',
      repo: 'wateryourtree'
    },

    // Credentials for user who leaves comments, etc.
    // You may want to load these from a seperate file like `config-credentials.js`, and
    // add this file to your `.gitignore` list
    login: {
      username: 'henryaspegren',
      password: 'marypoppins1'
    },

    // port for poppins to listen on and URL for Github to ping
    hook: {
      url: 'https://henry.locatunnel.me',
      port: 8000
    }
  };

  // load plugins from the cwd
  poppins.theUsualPlease();
  poppins.couldYouPlease('poppins-pr-checklist');

  // pr checklist
  poppins.plugins.prChecklist.greeting = 'Thank you for posing a PR!';
  poppins.plugins.prChecklist.checks = [
    { message: 'Does your PR commit meet the formatting guidelines?', condition: function (data) { return false; } },
    { message: 'Test Test', condition: function (data) { return true; } }
  ];
  poppins.plugins.prChecklist.closing = 'If you need to make changes to your PR....';


};
