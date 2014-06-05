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
      url: 'https://henry.localtunnel.me',
      port: 8000
    }
  };

  // load plugins from the cwd
  poppins.theUsualPlease();

  //  Run the checklist plugin
  poppins.couldYouPlease('poppins-pr-checklist');

  poppins.plugins.prChecklist.greeting = 'Hello';
  poppins.plugins.prChecklist.checks = [
    { message: 'Foo', condition: function (data) { return false; } }
  ];
  poppins.plugins.prChecklist.closing = 'Farewell';
};
