<template>
	<div class="p-6 bg-white">
		<form @submit.prevent="submitForm" class="space-y-8">
			<!-- Personal Information -->
			<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
				<!-- First Name -->
				<div>
					<label for="firstName" class="block text-sm font-medium text-gray-700 mb-2">
						First Name
					</label>
					<input
						id="firstName"
						v-model="form.first_name"
						type="text"
						placeholder="Enter first name"
						class="w-full px-3 py-2 border border-gray-300 rounded-sm shadow-sm placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
						required
					/>
				</div>

				<!-- Last Name -->
				<div>
					<label for="lastName" class="block text-sm font-medium text-gray-700 mb-2">
						Last Name
					</label>
					<input
						id="lastName"
						v-model="form.last_name"
						type="text"
						placeholder="Enter last name"
						class="w-full px-3 py-2 border border-gray-300 rounded-sm shadow-sm placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
						required
					/>
				</div>
			</div>

			<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
				<!-- Date of Birth -->
				<div>
					<label for="dateOfBirth" class="block text-sm font-medium text-gray-700 mb-2">
						Date of Birth
					</label>
					<input
						id="dateOfBirth"
						v-model="form.date_of_birth"
						type="date"
						class="w-full px-3 py-2 border border-gray-300 rounded-sm shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
						required
					/>
				</div>

				<!-- Gender -->
				<div>
					<label for="gender" class="block text-sm font-medium text-gray-700 mb-2">
						Gender
					</label>
					<select
						id="gender"
						v-model="form.gender"
						class="w-full px-3 py-2 border border-gray-300 rounded-sm shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 bg-white"
						required
					>
						<option value="" disabled>Select gender</option>
						<option value="male">Male</option>
						<option value="female">Female</option>
						<option value="other">Other</option>
						<option value="prefer-not-to-say">Prefer not to say</option>
					</select>
				</div>
			</div>

			<!-- Address -->
			<div>
				<label for="address" class="block text-sm font-medium text-gray-700 mb-2">
					Address
				</label>
				<textarea
					id="address"
					v-model="form.address"
					rows="3"
					placeholder="Enter address"
					class="w-full px-3 py-2 border border-gray-300 rounded-sm shadow-sm placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 resize-none"
				></textarea>
			</div>

			<!-- City, State, Zip Code -->
			<div class="grid grid-cols-1 md:grid-cols-3 gap-6">
				<!-- City -->
				<div>
					<label for="city" class="block text-sm font-medium text-gray-700 mb-2">
						City
					</label>
					<input
						id="city"
						v-model="form.city"
						type="text"
						placeholder="Enter city"
						class="w-full px-3 py-2 border border-gray-300 rounded-sm shadow-sm placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
					/>
				</div>

				<!-- State -->
				<div>
					<label for="state" class="block text-sm font-medium text-gray-700 mb-2">
						State
					</label>
					<input
						id="state"
						v-model="form.state"
						type="text"
						placeholder="Enter state"
						class="w-full px-3 py-2 border border-gray-300 rounded-sm shadow-sm placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
					/>
				</div>

				<!-- Zip Code -->
				<div>
					<label for="zipCode" class="block text-sm font-medium text-gray-700 mb-2">
						Zip Code
					</label>
					<input
						id="zipCode"
						v-model="form.zip_code"
						type="text"
						placeholder="Enter zip code"
						class="w-full px-3 py-2 border border-gray-300 rounded-sm shadow-sm placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
					/>
				</div>
			</div>

			<!-- Contact Information Section -->
			<div class="border-t pt-8">
				<h2 class="text-lg font-semibold text-gray-900 mb-6">Contact Information</h2>

				<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
					<!-- Email -->
					<div>
						<label for="email" class="block text-sm font-medium text-gray-700 mb-2">
							Email
						</label>
						<input
							id="email"
							v-model="form.email"
							type="email"
							placeholder="Enter email address"
							class="w-full px-3 py-2 border border-gray-300 rounded-sm shadow-sm placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
							required
						/>
					</div>

					<!-- Phone Number -->
					<div>
						<label
							for="phoneNumber"
							class="block text-sm font-medium text-gray-700 mb-2"
						>
							Phone Number
						</label>
						<input
							id="phoneNumber"
							v-model="form.phone_number"
							type="tel"
							placeholder="Enter phone number"
							class="w-full px-3 py-2 border border-gray-300 rounded-sm shadow-sm placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
							required
						/>
					</div>
				</div>

				<div class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-6">
					<!-- Emergency Contact Name -->
					<div>
						<label
							for="emergencyContactName"
							class="block text-sm font-medium text-gray-700 mb-2"
						>
							Emergency Contact Name
						</label>
						<input
							id="emergencyContactName"
							v-model="form.emergency_contact_name"
							type="text"
							placeholder="Enter emergency contact name"
							class="w-full px-3 py-2 border border-gray-300 rounded-sm shadow-sm placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
						/>
					</div>

					<!-- Emergency Contact Phone -->
					<div>
						<label
							for="emergencyContactPhone"
							class="block text-sm font-medium text-gray-700 mb-2"
						>
							Emergency Contact Phone
						</label>
						<input
							id="emergencyContactPhone"
							v-model="form.emergency_contact_phone"
							type="tel"
							placeholder="Enter emergency contact phone"
							class="w-full px-3 py-2 border border-gray-300 rounded-sm shadow-sm placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
						/>
					</div>
				</div>
			</div>

			<!-- Profile Photo Section -->
			<div>
				<h2 class="text-lg font-semibold mb-4">Profile Photo</h2>
				<div class="flex items-center space-x-4">
					<div>
						<input
							@change="handle_attachment($event)"
							type="file"
							name="fileToUpload"
							id="fileToUpload"
						/>
						<p class="text-sm text-gray-500 mt-1">
							Upload a profile photo. JPG, PNG or GIF. Max 2MB.
						</p>
					</div>
				</div>
			</div>
			<!-- Form Actions -->
			<div class="flex justify-end space-x-4 pt-8 border-t">
				<button
					type="button"
					@click="cancelForm"
					class="px-6 py-2 border border-gray-300 rounded-sm shadow-sm text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
				>
					Cancel
				</button>
				<button
					type="submit"
					:disabled="isSubmitting"
					class="px-6 py-2 border border-transparent rounded-sm shadow-sm text-sm font-medium text-white bg-gray-900 hover:bg-gray-800 focus:outline-none focus:ring-2 focus:ring-gray-500 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed"
				>
					<span v-if="isSubmitting">Saving...</span>
					<span v-else>Save Doctor</span>
				</button>
			</div>
		</form>
	</div>
</template>

<script setup>
import { ref, reactive } from 'vue'

// Form data
const form = reactive({
	first_name: '',
	last_name: '',
	date_of_birth: '',
	gender: '',
	address: '',
	city: '',
	state: '',
	zip_code: '',
	email: '',
	phone_number: '',
	emergency_contact_name: '',
	emergency_contact_phone: '',
	profile_photo: '',
	profile_photo_preview: null,
})

// Form state
const isSubmitting = ref(false)
const fileInput = ref(null)

// Methods

const submitForm = async () => {
	isSubmitting.value = true

	try {
		const formData = new FormData()

		// Append all form fields to FormData
		Object.keys(form).forEach((key) => {
			if (key !== 'profilePhotoPreview' && form[key] !== null) {
				formData.append(key, form[key])
			}
		})

		// 🔄 Call your API here
		const response = await fetch(
			'http://hosp.localhost:8000/api/method/bharat_med.api.register_doctor',
			{
				method: 'POST',
				body: formData,
			},
		)

		if (!response.ok) {
			throw new Error('Network response was not ok')
		}

		// Optional: handle response data
		const result = await response.json()
		console.log('API Response:', result)

		alert('Doctor saved successfully!')
		resetForm()
	} catch (error) {
		console.error('Error submitting form:', error)
		alert('Error saving doctor. Please try again.')
	} finally {
		isSubmitting.value = false
	}
}
const handle_attachment = (event) => {
	const file = event.target.files[0]
	if (file) {
		const reader = new FileReader()
		reader.onload = (e) => {
			form.profile_photo = e.target.result // base64 string
		}
		reader.readAsDataURL(file)
	}
}
const cancelForm = () => {
	if (confirm('Are you sure you want to cancel? All unsaved changes will be lost.')) {
		resetForm()
	}
}

const resetForm = () => {
	Object.keys(form).forEach((key) => {
		if (key === 'profilePhoto' || key === 'profilePhotoPreview') {
			form[key] = null
		} else {
			form[key] = ''
		}
	})

	if (fileInput.value) {
		fileInput.value.value = ''
	}
}

// Set default date to today
const today = new Date().toISOString().split('T')[0]
form.dateOfBirth = today
</script>

<style scoped>
/* Additional custom styles if needed */
.sr-only {
	position: absolute;
	width: 1px;
	height: 1px;
	padding: 0;
	margin: -1px;
	overflow: hidden;
	clip: rect(0, 0, 0, 0);
	white-space: nowrap;
	border: 0;
}
</style>
