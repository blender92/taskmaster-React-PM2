module.exports = {
	apps: [
		{
			name: 'my_react_app',
			script: 'npm',
			args: 'run start:production',
			env_production: {
				NODE_ENV: 'production',
			},
		},
	],

	deploy: {
		production: {
			user: 'node',
			host: '212.32.248.106',
			ref: 'main',
			repo: 'git@github.com:blender92/taskmaster-react.git',
			path: '/var/www/react/',
			'pre-deploy-local': '',
			'post-deploy':
				'npm install && pm2 reload ecosystem.config.js --env production',
			'pre-setup': '',
		},
	},
};
