<template>
	<div class="m-3 flex flex-row items-center justify-center">
		<Card title="Login to your FrappeUI App!" class="w-full max-w-md mt-4">
			<form class="flex flex-col space-y-2 w-full" @submit.prevent="submit">
				<Input
					required
					name="email"
					type="text"
					placeholder="johndoe@email.com"
					label="User ID"
				/>
				<Input
					required
					name="password"
					type="password"
					placeholder="••••••"
					label="Password"
				/>
				<div class="flex items-center justify-between mt-4">
					<p class="text-sm text-gray-600">
						Don't have an account?
						<a href="/register" class="text-blue-600 hover:underline font-medium"
							>Register</a
						>
					</p>
				</div>
				<Button :loading="session.login.loading" variant="solid">Login</Button>
			</form>
		</Card>
	</div>
</template>

<script lang="ts" setup>
import { session } from '../Service/auth.js'

function submit(e) {
	let formData = new FormData(e.target)
	session.login.submit({
		email: formData.get('email'),
		password: formData.get('password'),
	})
}
</script>
