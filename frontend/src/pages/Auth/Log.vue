<template>
	<div
		class="flex pt-[62px] flex-col items-center min-h-screen bg-secondary"
		style="background: #f5f5f5"
	>
		<!-- Main Content Centered -->
		<main
			class="flex flex-col items-center text-center w-full px-4 min-h-[calc(100vh-64px)] justify-center"
		>
			<div class="mt-8 bg-white p-6 rounded-sm w-full max-w-[443px] shadow-md">
				<h2 class="text-[20px] font-medium mb-4">Login to your account</h2>
				<input
					type="email"
					v-model="email"
					placeholder="sample@example.com"
					class="w-full p-2 border rounded-sm mb-4 text-[14px]"
					style="color: #6e7073"
					@keyup.enter="get_otp()"
				/>
				<button
					:disabled="loading"
					@click="get_otp()"
					class="w-full flex items-center justify-center text-white py-2 rounded-sm text-bodyh2"
					style="background: #001f3f"
				>
					<div class="h-5 w-5" v-if="loading">
						<div
							class="animate-spin h-full w-full rounded-full border-[2px] flex justify-center items-center border-dotted border-[#fff]"
						>
							<div
								class="w-3 h-3 rounded-full border-dashed border-[1px] border-[#fff]"
							></div>
						</div>
					</div>
					<p v-else>GET OTP</p>
				</button>
				<p class="text-bodyh2 mt-4 text-gray-600">
					Don't have an account?
					<router-link to="/register" class="text-[#001f3f]">Sign up</router-link>
				</p>
				<div class="flex items-center my-4">
					<hr class="flex-grow border-t border-gray-300" />
					<span class="mx-2 text-gray-500 text-caption">OR</span>
					<hr class="flex-grow border-t border-gray-300" />
				</div>
				<div class="mt-4">
					<a :href="g_url">
						<button
							class="w-full flex items-center justify-start p-2 border rounded-sm mb-2 text-bodyh2 font-normal"
							@click="Google_login"
						>
							<img
								src="../../assets/icons8-google-48.png"
								alt="Google"
								class="h-5 mr-2"
							/>
							Continue with Google
						</button>
					</a>

					<a :href="m_url">
						<button
							class="w-full flex items-center justify-start p-2 border rounded-sm text-bodyh2"
							@click="micro_login"
						>
							<img
								src="../../assets/icons8-microsoft-48.png"
								alt="Microsoft"
								class="h-5 mr-2"
							/>
							Continue with Microsoft
						</button>
					</a>
				</div>
			</div>
		</main>
	</div>
</template>

<script setup>
import { ref, inject, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { toast } from 'vue3-toastify'
import 'vue3-toastify/dist/index.css'

const call = inject('call')
const router = useRouter()
const route = useRoute()
const email = ref('')
const loading = ref(false)
const g_url = ref('')
const m_url = ref('')

const get_otp = async () => {
	console.log('get_otp called with email:', email.value)

	if (email.value === '') {
		toast.error('Email is required')
		return
	}
	console.log('Sending OTP to:', email.value)

	let url = ''
	if (route.query.full_name) {
		url = 'register_send_otp'
		console.log('Registering new user, using register_send_otp endpoint', url)
	} else {
		url = 'send_otp'
	}
	console.log('Using URL:', url)

	try {
		loading.value = true
		const response = await fetch(
			`http://hosp.localhost:8000/api/method/bharat_med.controllers.email.${url}`,
			{
				method: 'POST',
				headers: {
					'Content-Type': 'application/json',
				},
				body: JSON.stringify({
					email: email.value,
				}),
			},
		)
		console.log('Response from server:', response)
		if (response.status === 200) {
			loading.value = false
			toast.success('OTP sent successfully', {
				position: 'top-right',
				autoClose: 2000,
				hideProgressBar: false,
				closeOnClick: true,
				pauseOnHover: true,
			})
			setTimeout(() => {
				router.push({
					name: 'Otp',
					query: {
						email: email.value,
						returnUrl: route.query.returnUrl, // Preserve any return URL if present
					},
				})
			}, 2000)
		} else {
			loading.value = false
			toast.error(response.message, {
				position: 'top-right',
				autoClose: 2000,
				hideProgressBar: false,
				closeOnClick: true,
				pauseOnHover: true,
			})
		}
	} catch (error) {
		toast.error('Something went wrong', {
			position: 'top-right',
			autoClose: 2000,
			hideProgressBar: false,
			closeOnClick: true,
			pauseOnHover: true,
		})
	}
}

// const get = async () => {
// 	const response = await call('bharat_med.controllers.api.get_login_details')
// 	g_url.value = response[0].google_login_url
// 	m_url.value = response[0].office_365_login_url
// }

// Log text when the page loads
// onMounted(async () => {
// 	console.log('Page has loaded')
// 	await get() // Fetch login details on page load
// })
</script>
