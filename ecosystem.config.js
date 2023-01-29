module.exports = {
	apps: [
		{
			script: 'index.js',
			watch: '.',
		},
		{
			script: './service-worker/',
			watch: ['./service-worker'],
		},
	],

	deploy: {
		production: {
			user: 'node',
			host: '212.32.248.106',
			ref: 'origin/master',
			repo: 'https://github.com/blender92/taskmaster-react',
			path: '/var/www/react/',
			'pre-deploy-local': '',
			'post-deploy':
				'npm install && pm2 reload ecosystem.config.js --env production',
			'pre-setup': '',
		},
	},
};
