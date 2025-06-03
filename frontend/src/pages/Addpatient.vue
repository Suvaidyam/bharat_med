<template>
	<div class="min-h-screen p-4">
		<!-- Header -->
		<div class="mb-6">
			<div class="flex items-center gap-4 mb-2">
				<button
					@click="goBack"
					class="p-2 hover:bg-gray-100 rounded-sm transition-colors duration-200"
				>
					<svg
						class="w-5 h-5 text-gray-600"
						fill="none"
						stroke="currentColor"
						viewBox="0 0 24 24"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M15 19l-7-7 7-7"
						></path>
					</svg>
				</button>
				<div>
					<h1 class="text-2xl sm:text-3xl font-bold text-gray-900">Add Patient</h1>
					<p class="text-gray-600 mt-1">Register a new patient in your clinic.</p>
				</div>
			</div>
		</div>

		<!-- Form Container -->
		<div class="bg-white rounded-sm shadow-sm border border-gray-200">
			<!-- Tabs -->
			<div class="border-b border-gray-200">
				<nav class="flex space-x-8 px-6" aria-label="Tabs">
					<button
						v-for="tab in tabs"
						:key="tab.id"
						@click="activeTab = tab.id"
						:class="[
							'py-4 px-1 border-b-2 font-medium text-sm transition-colors duration-200',
							activeTab === tab.id
								? 'border-black text-black'
								: 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300',
						]"
					>
						{{ tab.name }}
					</button>
				</nav>
			</div>

			<!-- Form Content -->
			<div class="p-6">
				<!-- Personal Information Tab -->
				<div v-if="activeTab === 'personal'" class="space-y-8">
					<!-- Personal Information Section -->
					<div>
						<h2 class="text-lg font-semibold text-gray-900 mb-2">
							Personal Information
						</h2>
						<p class="text-gray-600 mb-6">Enter the patient's personal details.</p>

						<div class="grid grid-cols-1 md:grid-cols-3 gap-6">
							<!-- First Name -->
							<div>
								<label
									for="first_name"
									class="block text-sm font-medium text-gray-700 mb-2"
								>
									First Name
								</label>
								<input
									id="first_name"
									v-model="form.first_name"
									type="text"
									placeholder="Enter first name"
									class="w-full px-3 py-2 border border-gray-300 rounded-sm focus:ring-2 focus:ring-blue-500 focus:border-transparent"
								/>
							</div>

							<!-- Middle Name -->
							<div>
								<label
									for="middle_name"
									class="block text-sm font-medium text-gray-700 mb-2"
								>
									Middle Name (Optional)
								</label>
								<input
									id="middle_name"
									v-model="form.middle_name"
									type="text"
									placeholder="Enter middle name"
									class="w-full px-3 py-2 border border-gray-300 rounded-sm focus:ring-2 focus:ring-blue-500 focus:border-transparent"
								/>
							</div>

							<!-- Last Name -->
							<div>
								<label
									for="last_name"
									class="block text-sm font-medium text-gray-700 mb-2"
								>
									Last Name
								</label>
								<input
									id="last_name"
									v-model="form.last_name"
									type="text"
									placeholder="Enter last name"
									class="w-full px-3 py-2 border border-gray-300 rounded-sm focus:ring-2 focus:ring-blue-500 focus:border-transparent"
								/>
							</div>
						</div>

						<div class="grid grid-cols-1 md:grid-cols-3 gap-6 mt-6">
							<!-- Date of Birth -->
							<div>
								<label
									for="date_of_birth"
									class="block text-sm font-medium text-gray-700 mb-2"
								>
									Date of Birth
								</label>
								<input
									id="date_of_birth"
									v-model="form.date_of_birth"
									type="date"
									class="w-full px-3 py-2 border border-gray-300 rounded-sm focus:ring-2 focus:ring-blue-500 focus:border-transparent"
								/>
							</div>

							<!-- Gender -->
							<div>
								<label
									for="gender"
									class="block text-sm font-medium text-gray-700 mb-2"
								>
									Gender
								</label>
								<select
									id="gender"
									v-model="form.gender"
									class="w-full px-3 py-2 border border-gray-300 rounded-sm focus:ring-2 focus:ring-blue-500 focus:border-transparent"
								>
									<option value="">Select gender</option>
									<option value="Male">Male</option>
									<option value="Female">Female</option>
									<option value="Other">Other</option>
								</select>
							</div>

							<!-- Marital Status -->
							<div>
								<label
									for="marital_status"
									class="block text-sm font-medium text-gray-700 mb-2"
								>
									Marital Status
								</label>
								<select
									id="marital_status"
									v-model="form.marital_status"
									class="w-full px-3 py-2 border border-gray-300 rounded-sm focus:ring-2 focus:ring-blue-500 focus:border-transparent"
								>
									<option value="">Select status</option>
									<option value="Single">Single</option>
									<option value="Married">Married</option>
									<option value="Divorced">Divorced</option>
									<option value="Widowed">Widowed</option>
									<option value="Separated">Separated</option>
								</select>
							</div>
						</div>

						<!-- Address -->
						<div class="mt-6">
							<label
								for="address"
								class="block text-sm font-medium text-gray-700 mb-2"
							>
								Address
							</label>
							<textarea
								id="address"
								v-model="form.address"
								rows="3"
								placeholder="Enter address"
								class="w-full px-3 py-2 border border-gray-300 rounded-sm focus:ring-2 focus:ring-blue-500 focus:border-transparent"
							></textarea>
						</div>

						<div class="grid grid-cols-1 md:grid-cols-3 gap-6 mt-6">
							<!-- City -->
							<div>
								<label
									for="city"
									class="block text-sm font-medium text-gray-700 mb-2"
								>
									City
								</label>
								<input
									id="city"
									v-model="form.city"
									type="text"
									placeholder="Enter city"
									class="w-full px-3 py-2 border border-gray-300 rounded-sm focus:ring-2 focus:ring-blue-500 focus:border-transparent"
								/>
							</div>

							<!-- State -->
							<div>
								<label
									for="state"
									class="block text-sm font-medium text-gray-700 mb-2"
								>
									State
								</label>
								<input
									id="state"
									v-model="form.state"
									type="text"
									placeholder="Enter state"
									class="w-full px-3 py-2 border border-gray-300 rounded-sm focus:ring-2 focus:ring-blue-500 focus:border-transparent"
								/>
							</div>

							<!-- Zip Code -->
							<div>
								<label
									for="zip_code"
									class="block text-sm font-medium text-gray-700 mb-2"
								>
									Zip Code
								</label>
								<input
									id="zip_code"
									v-model="form.zip_code"
									type="text"
									placeholder="Enter zip code"
									class="w-full px-3 py-2 border border-gray-300 rounded-sm focus:ring-2 focus:ring-blue-500 focus:border-transparent"
								/>
							</div>
						</div>
					</div>

					<!-- Contact Information Section -->
					<div>
						<h2 class="text-lg font-semibold text-gray-900 mb-6">
							Contact Information
						</h2>

						<div class="grid grid-cols-1 md:grid-cols-3 gap-6">
							<!-- Email -->
							<div>
								<label
									for="email"
									class="block text-sm font-medium text-gray-700 mb-2"
								>
									Email
								</label>
								<input
									id="email"
									v-model="form.email"
									type="email"
									placeholder="Enter email address"
									class="w-full px-3 py-2 border border-gray-300 rounded-sm focus:ring-2 focus:ring-blue-500 focus:border-transparent"
								/>
							</div>

							<!-- Phone Number -->
							<div>
								<label
									for="phone_number"
									class="block text-sm font-medium text-gray-700 mb-2"
								>
									Phone Number
								</label>
								<input
									id="phone_number"
									v-model="form.phone_number"
									type="tel"
									placeholder="Enter phone number"
									class="w-full px-3 py-2 border border-gray-300 rounded-sm focus:ring-2 focus:ring-blue-500 focus:border-transparent"
								/>
							</div>

							<!-- Alternative Phone -->
							<div>
								<label
									for="alternative_phone"
									class="block text-sm font-medium text-gray-700 mb-2"
								>
									Alternative Phone (Optional)
								</label>
								<input
									id="alternative_phone"
									v-model="form.alternative_phone"
									type="tel"
									placeholder="Enter alternative phone"
									class="w-full px-3 py-2 border border-gray-300 rounded-sm focus:ring-2 focus:ring-blue-500 focus:border-transparent"
								/>
							</div>
						</div>
					</div>
					<!-- <div class="mb-6">
						  <label class="block font-semibold mb-2">Preferred Contact Method</label>
						  <div class="space-y-2">
							  <label class="flex items-center space-x-2">
								  <input type="radio" v-model="preferredContact" value="Phone" />
								  <span>Phone</span>
							  </label>
							  <label class="flex items-center space-x-2">
								  <input type="radio" v-model="preferredContact" value="Email" />
								  <span>Email</span>
							  </label>
							  <label class="flex items-center space-x-2">
								  <input type="radio" v-model="preferredContact" value="SMS" />
								  <span>SMS</span>
							  </label>
						  </div>
					  </div> -->

					<hr class="my-6" />

					<!-- Emergency Contact -->
					<div class="mb-6">
						<h2 class="text-lg font-semibold mb-4">Emergency Contact</h2>
						<div class="grid md:grid-cols-2 gap-4">
							<div>
								<label class="block mb-1 font-medium" for="contact_name"
									>Contact Name</label
								>
								<input
									type="text"
									id="contact_name"
									v-model="form.contact_name"
									class="w-full rounded-sm px-3 py-2 border border-gray-300"
									placeholder="Enter emergency contact name"
								/>
							</div>
							<div>
								<label class="block mb-1 font-medium" for="relationship"
									>Relationship</label
								>
								<input
									type="text"
									id="relationship"
									v-model="form.relationship"
									class="w-full rounded-sm px-3 py-2 border border-gray-300"
									placeholder="Enter relationship"
								/>
							</div>
							<div>
								<label class="block mb-1 font-medium" for="emergency_phone"
									>Phone Number</label
								>
								<input
									type="text"
									id="emergency_phone"
									v-model="form.emergency_phone"
									class="w-full rounded-sm px-3 py-2 border border-gray-300"
									placeholder="Enter emergency contact phone"
								/>
							</div>
							<div>
								<label class="block mb-1 font-medium" for="emergency_email"
									>Email (Optional)</label
								>
								<input
									type="email"
									id="emergency_email"
									v-model="form.emergency_email"
									class="w-full rounded-sm px-3 py-2 border border-gray-300"
									placeholder="Enter emergency contact email"
								/>
							</div>
						</div>
					</div>

					<hr class="my-6" />

					<!-- Profile Photo Upload -->
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
				</div>

				<!-- Medical Information Tab -->
				<div v-else-if="activeTab === 'medical'" class="space-y-6">
					<div>
						<h2 class="text-lg font-semibold text-gray-900 mb-2">
							Medical Information
						</h2>
						<p class="text-gray-600 mb-6">
							Enter the patient's medical details and history.
						</p>

						<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
							<div>
								<label
									for="bloodType"
									class="block text-sm font-medium text-gray-700 mb-2"
								>
									Blood Type
								</label>
								<select
									id="bloodType"
									v-model="form.bloodType"
									class="w-full px-3 py-2 border border-gray-300 rounded-sm focus:ring-2 focus:ring-blue-500 focus:border-transparent"
								>
									<option value="">Select blood type</option>
									<option value="A+">A+</option>
									<option value="A-">A-</option>
									<option value="B+">B+</option>
									<option value="B-">B-</option>
									<option value="AB+">AB+</option>
									<option value="AB-">AB-</option>
									<option value="O+">O+</option>
									<option value="O-">O-</option>
								</select>
							</div>

							<div>
								<label
									for="emergencyContact"
									class="block text-sm font-medium text-gray-700 mb-2"
								>
									Emergency Contact
								</label>
								<input
									id="emergencyContact"
									v-model="form.emergencyContact"
									type="text"
									placeholder="Enter emergency contact"
									class="w-full px-3 py-2 border border-gray-300 rounded-sm focus:ring-2 focus:ring-blue-500 focus:border-transparent"
								/>
							</div>
						</div>

						<div class="mt-6">
							<label
								for="allergies"
								class="block text-sm font-medium text-gray-700 mb-2"
							>
								Allergies
							</label>
							<textarea
								id="allergies"
								v-model="form.allergies"
								rows="3"
								placeholder="Enter known allergies"
								class="w-full px-3 py-2 border border-gray-300 rounded-sm focus:ring-2 focus:ring-blue-500 focus:border-transparent"
							></textarea>
						</div>

						<div class="mt-6">
							<label
								for="medicalHistory"
								class="block text-sm font-medium text-gray-700 mb-2"
							>
								Medical History
							</label>
							<textarea
								id="medicalHistory"
								v-model="form.medicalHistory"
								rows="4"
								placeholder="Enter medical history"
								class="w-full px-3 py-2 border border-gray-300 rounded-sm focus:ring-2 focus:ring-blue-500 focus:border-transparent"
							></textarea>
						</div>
					</div>
				</div>

				<!-- Insurance & Billing Tab -->
				<div v-else-if="activeTab === 'insurance'" class="space-y-6">
					<div>
						<h2 class="text-lg font-semibold text-gray-900 mb-2">
							Insurance & Billing
						</h2>
						<p class="text-gray-600 mb-6">Enter insurance and billing information.</p>

						<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
							<div>
								<label
									for="insuranceProvider"
									class="block text-sm font-medium text-gray-700 mb-2"
								>
									Insurance Provider
								</label>
								<input
									id="insuranceProvider"
									v-model="form.insuranceProvider"
									type="text"
									placeholder="Enter insurance provider"
									class="w-full px-3 py-2 border border-gray-300 rounded-sm focus:ring-2 focus:ring-blue-500 focus:border-transparent"
								/>
							</div>

							<div>
								<label
									for="policyNumber"
									class="block text-sm font-medium text-gray-700 mb-2"
								>
									Policy Number
								</label>
								<input
									id="policyNumber"
									v-model="form.policyNumber"
									type="text"
									placeholder="Enter policy number"
									class="w-full px-3 py-2 border border-gray-300 rounded-sm focus:ring-2 focus:ring-blue-500 focus:border-transparent"
								/>
							</div>
						</div>
					</div>
				</div>

				<!-- Consent & Documents Tab -->
				<div v-else-if="activeTab === 'consent'" class="space-y-6">
					<div>
						<h2 class="text-lg font-semibold text-gray-900 mb-2">
							Consent & Documents
						</h2>
						<p class="text-gray-600 mb-6">Patient consent and document uploads.</p>

						<div class="space-y-4">
							<div class="flex items-start">
								<input
									id="treatmentConsent"
									v-model="form.treatmentConsent"
									type="checkbox"
									class="mt-1 h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded"
								/>
								<label for="treatmentConsent" class="ml-3 text-sm text-gray-700">
									I consent to treatment and procedures as recommended by the
									healthcare provider.
								</label>
							</div>

							<div class="flex items-start">
								<input
									id="privacyConsent"
									v-model="form.privacyConsent"
									type="checkbox"
									class="mt-1 h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded"
								/>
								<label for="privacyConsent" class="ml-3 text-sm text-gray-700">
									I acknowledge that I have read and understand the privacy
									policy.
								</label>
							</div>
						</div>
					</div>
				</div>
			</div>

			<!-- Form Actions -->
			<div
				class="px-6 py-4 border-t border-gray-200 flex flex-col sm:flex-row justify-end gap-3"
			>
				<button
					@click="goBack"
					type="button"
					class="px-6 py-2 border border-gray-300 rounded-sm text-gray-700 hover:bg-gray-50 transition-colors duration-200 font-medium"
				>
					Cancel
				</button>
				<button
					@click="savePatient"
					type="button"
					class="px-6 py-2 bg-black text-white rounded-sm hover:bg-gray-800 transition-colors duration-200 font-medium"
				>
					Save Patient
				</button>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, reactive } from 'vue'

const activeTab = ref('personal')

const tabs = [
	{ id: 'personal', name: 'Personal Information' },
	{ id: 'medical', name: 'Medical Information' },
	{ id: 'insurance', name: 'Insurance & Billing' },
	{ id: 'consent', name: 'Consent & Documents' },
]

const form = reactive({
	// Personal Information
	first_name: '',
	middle_name: '',
	last_name: '',
	date_of_birth: '',
	gender: '',
	marital_status: '',
	address: '',
	city: '',
	state: '',
	zip_code: '',

	// Contact Information
	email: '',
	phone_number: '',
	alternative_phone: '',
	contact_name: '',
	relationship: '',
	emergency_phone: '',
	emergency_email: '',
	profile_photo: '',
})

const goBack = () => {
	// Handle navigation back to patient list
	console.log('Going back to patient list')
}

const savePatient = async () => {
	try {
		const response = await fetch(
			'http://hosp.localhost:8000/api/method/bharat_med.api.register_patient',
			{
				method: 'POST',
				headers: {
					'Content-Type': 'application/json',
				},
				body: JSON.stringify({
					...form,
					profilePhoto: form.profilePhoto, // Assuming profilePhoto is a file input
					// Handle profile photo upload separately
					// You might need to convert it to a Blob or FormData
					// before sending if it's a file input
					// Otherwise, send the URL or base64 string directly
				}),
			},
		)

		const data = await response.json()
		console.log(data)

		if (response.ok && data.message) {
			toast.success('Patient registered successfully!', { autoClose: 3000 })

			// Reset form after successful registration
			Object.keys(form).forEach((key) => {
				form[key] = ''
			})
			// Optionally reset profile photo if needed
			profilePhoto.value = ''
			// Show success message
			console.log('Patient registered successfully:', data.message)
			// Navigate if needed
			setTimeout(() => {
				router.push('/patients')
			}, 2000)
		} else {
			toast.error(`Error: ${data.error || 'Registration failed'}`, {
				autoClose: 3000,
			})
		}
	} catch (error) {
		toast.error(`Error: ${error.message}`, { autoClose: 3000 })
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
</script>
