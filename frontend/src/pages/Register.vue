<template>
	<div class="min-h-screen flex items-center justify-center bg-gray-100 px-4">
		<div class="max-w-md w-full bg-white p-8 rounded-xl shadow-lg">
			<h2 class="text-2xl font-bold text-center text-gray-800 mb-6">User Registration</h2>
			<form @submit.prevent="register">
				<div class="mb-4">
					<label class="block text-gray-700 font-medium mb-1">First Name</label>
					<input
						type="text"
						v-model="firstName"
						required
						class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring focus:ring-blue-300"
					/>
				</div>
				<div class="mb-4">
					<label class="block text-gray-700 font-medium mb-1">Email</label>
					<input
						type="email"
						v-model="email"
						required
						class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring focus:ring-blue-300"
					/>
				</div>
				<div class="mb-4">
					<label class="block text-gray-700 font-medium mb-1">Mobile</label>
					<input
						type="tel"
						v-model="mobile"
						required
						class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring focus:ring-blue-300"
					/>
				</div>
				<div class="mb-4">
					<label class="block text-gray-700 font-medium mb-1">Password</label>
					<input
						type="password"
						v-model="password"
						required
						class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring focus:ring-blue-300"
					/>
				</div>
				<div class="mb-4">
					<label class="block text-gray-700 font-medium mb-1">Confirm Password</label>
					<input
						type="password"
						v-model="confirmPassword"
						required
						class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring focus:ring-blue-300"
					/>
				</div>
				<div class="mb-6">
					<label class="block text-gray-700 font-medium mb-1">Role</label>
					<select
						v-model="role"
						required
						class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring focus:ring-blue-300"
					>
						<option value="">Select Role</option>
						<option value="Doctor">Doctor</option>
						<option value="Patient">Patient</option>
					</select>
				</div>
				<button
					type="submit"
					class="w-full bg-[#001f3f] text-white py-2 rounded-lg hover:bg-[#0f375f]"
				>
					Register
				</button>
			</form>
		</div>
	</div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { ref } from 'vue'
import { toast } from 'vue3-toastify'
import 'vue3-toastify/dist/index.css'
const firstName = ref('')
const email = ref('')
const mobile = ref('')
const password = ref('')
const confirmPassword = ref('')
const role = ref('')
const router = useRouter()
const register = async () => {
	if (password.value !== confirmPassword.value) {
		toast.error('Passwords do not match.', { autoClose: 5000 })
		return
	}

	try {
		const response = await fetch(
			'http://hosp.localhost:8000/api/method/bharat_med.api.register_user',
			{
				method: 'POST',
				headers: {
					'Content-Type': 'application/json',
				},
				body: JSON.stringify({
					first_name: firstName.value,
					email: email.value,
					mobile: mobile.value,
					password: password.value,
					confirm_password: confirmPassword.value,
					role_profile: role.value,
				}),
			},
		)

		const data = await response.json()
		console.log(data)

		if (response.ok && data.message) {
			toast.success('Registration successful! Please log in.', { autoClose: 5000 })

			firstName.value = ''
			email.value = ''
			mobile.value = ''
			password.value = ''
			confirmPassword.value = ''
			role.value = ''
			setTimeout(() => {
				router.push('/login')
			}, 50000)
		} else {
			toast.error(`Error: ${data.error || 'Something went wrong'}`, { autoClose: 5000 })
		}
	} catch (error) {
		toast.error(`Error: ${error.message}`, { autoClose: 5000 })
	}
}
</script>
