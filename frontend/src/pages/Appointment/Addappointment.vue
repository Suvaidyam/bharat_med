<template>
	<div class="min-h-screen bg-white p-4 md:p-6">
		<div class="">
			<!-- Header -->
			<div class="flex items-center mb-6">
				<button
					@click="goBack"
					class="mr-4 p-2 rounded-sm hover:bg-gray-200 transition-colors"
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
					<h1 class="text-2xl md:text-3xl font-bold text-gray-900">Add Appointment</h1>
					<p class="text-gray-600 mt-1">Schedule a new appointment for a patient.</p>
				</div>
			</div>

			<!-- Form Layout -->
			<div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
				<!-- Left Column - Appointment Details -->
				<div class="lg:col-span-2">
					<div class="bg-white rounded-lg shadow p-6">
						<h2 class="text-lg font-semibold text-gray-900 mb-2">
							Appointment Details
						</h2>
						<p class="text-gray-600 mb-6">
							Enter the details for the new appointment.
						</p>

						<form @submit.prevent="submitAppointment" class="space-y-6">
							<!-- Appointment Type -->
							<div>
								<label
									for="appointmentType"
									class="block text-sm font-medium text-gray-700 mb-2"
								>
									Appointment Type
								</label>
								<select
									id="appointmentType"
									v-model="form.appointmentType"
									class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
									required
								>
									<option value="">Select appointment type</option>
									<option value="consultation">Consultation</option>
									<option value="checkup">Check-up</option>
									<option value="follow-up">Follow-up</option>
									<option value="dental-cleaning">Dental Cleaning</option>
									<option value="vaccination">Vaccination</option>
									<option value="x-ray">X-Ray</option>
									<option value="therapy">Therapy Session</option>
									<option value="annual-physical">Annual Physical</option>
								</select>
							</div>

							<!-- Date -->
							<div>
								<label
									for="date"
									class="block text-sm font-medium text-gray-700 mb-2"
								>
									Date
								</label>
								<input
									id="date"
									v-model="form.date"
									type="date"
									class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
									required
								/>
							</div>

							<!-- Time -->
							<div>
								<label
									for="time"
									class="block text-sm font-medium text-gray-700 mb-2"
								>
									Time
								</label>
								<select
									id="time"
									v-model="form.time"
									class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
									required
								>
									<option value="">Select time slot</option>
									<option
										v-for="timeSlot in timeSlots"
										:key="timeSlot"
										:value="timeSlot"
									>
										{{ timeSlot }}
									</option>
								</select>
							</div>

							<!-- Duration -->
							<div>
								<label
									for="duration"
									class="block text-sm font-medium text-gray-700 mb-2"
								>
									Duration (minutes)
								</label>
								<select
									id="duration"
									v-model="form.duration"
									class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
									required
								>
									<option value="">Select duration</option>
									<option value="15">15 minutes</option>
									<option value="30">30 minutes</option>
									<option value="45">45 minutes</option>
									<option value="60">60 minutes</option>
									<option value="90">90 minutes</option>
								</select>
							</div>

							<!-- Reason for Visit -->
							<div>
								<label
									for="reason"
									class="block text-sm font-medium text-gray-700 mb-2"
								>
									Reason for Visit
								</label>
								<textarea
									id="reason"
									v-model="form.reason"
									rows="4"
									placeholder="Enter the reason for the appointment"
									class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-none"
								></textarea>
							</div>

							<!-- Appointment Status -->
							<div>
								<label class="block text-sm font-medium text-gray-700 mb-3">
									Appointment Status
								</label>
								<div class="space-y-3">
									<label class="flex items-center">
										<input
											v-model="form.status"
											type="radio"
											value="scheduled"
											class="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300"
										/>
										<span class="ml-2 text-sm text-gray-700">Scheduled</span>
									</label>
									<label class="flex items-center">
										<input
											v-model="form.status"
											type="radio"
											value="tentative"
											class="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300"
										/>
										<span class="ml-2 text-sm text-gray-700"
											>Tentative (Pending Confirmation)</span
										>
									</label>
									<label class="flex items-center">
										<input
											v-model="form.status"
											type="radio"
											value="waitlist"
											class="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300"
										/>
										<span class="ml-2 text-sm text-gray-700"
											>Add to Waitlist</span
										>
									</label>
								</div>
							</div>
							<div>
								<label class="block text-sm font-medium text-gray-700 mb-3">
									Addiional Information
								</label>
								<label for="">Notes for Staff</label>
								<textarea
									v-model="form.additionalInfo"
									rows="4"
									placeholder="Enter any additional information or notes"
									class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-none"
								></textarea>
							</div>

							<!-- Action Buttons -->
							<div class="flex flex-col sm:flex-row gap-3 pt-6">
								<button
									type="button"
									@click="goBack"
									class="flex-1 bg-gray-200 text-gray-700 py-2 px-4 rounded-md hover:bg-gray-300 focus:outline-none focus:ring-2 focus:ring-gray-500 focus:ring-offset-2 transition-colors"
								>
									Cancel
								</button>
								<button
									type="submit"
									class="flex-1 bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 transition-colors"
								>
									Schedule Appointment
								</button>
							</div>
						</form>
					</div>
				</div>

				<!-- Right Column - Patient & Doctor Selection -->
				<div class="space-y-6">
					<!-- Select Patient -->
					<div class="bg-white rounded-lg shadow p-6">
						<h2 class="text-lg font-semibold text-gray-900 mb-2">Select Patient</h2>
						<p class="text-gray-600 mb-4">
							Search and select a patient for this appointment.
						</p>

						<div class="space-y-4">
							<div class="relative">
								<input
									v-model="patientSearch"
									type="text"
									placeholder="Search patients..."
									class="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
									@input="searchPatients"
								/>
								<svg
									class="absolute left-3 top-2.5 h-5 w-5 text-gray-400"
									fill="none"
									stroke="currentColor"
									viewBox="0 0 24 24"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										stroke-width="2"
										d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
									></path>
								</svg>
							</div>

							<!-- Patient Results -->
							<div
								v-if="filteredPatients.length > 0"
								class="max-h-48 overflow-y-auto border border-gray-200 rounded-md"
							>
								<div
									v-for="patient in filteredPatients"
									:key="patient.id"
									@click="selectPatient(patient)"
									class="flex items-center p-3 hover:bg-gray-50 cursor-pointer border-b border-gray-100 last:border-b-0"
									:class="{
										'bg-blue-50 border-blue-200':
											selectedPatient?.id === patient.id,
									}"
								>
									<img
										:src="patient.avatar"
										:alt="patient.name"
										class="h-8 w-8 rounded-full"
									/>
									<div class="ml-3">
										<p class="text-sm font-medium text-gray-900">
											{{ patient.name }}
										</p>
										<p class="text-xs text-gray-500">{{ patient.email }}</p>
									</div>
								</div>
							</div>

							<!-- Selected Patient Display -->
							<div
								v-if="selectedPatient"
								class="bg-blue-50 border border-blue-200 rounded-md p-3"
							>
								<div class="flex items-center">
									<img
										:src="selectedPatient.avatar"
										:alt="selectedPatient.name"
										class="h-8 w-8 rounded-full"
									/>
									<div class="ml-3 flex-1">
										<p class="text-sm font-medium text-gray-900">
											{{ selectedPatient.name }}
										</p>
										<p class="text-xs text-gray-500">
											{{ selectedPatient.email }}
										</p>
									</div>
									<button
										@click="clearPatientSelection"
										class="text-gray-400 hover:text-gray-600"
									>
										<svg
											class="w-4 h-4"
											fill="none"
											stroke="currentColor"
											viewBox="0 0 24 24"
										>
											<path
												stroke-linecap="round"
												stroke-linejoin="round"
												stroke-width="2"
												d="M6 18L18 6M6 6l12 12"
											></path>
										</svg>
									</button>
								</div>
							</div>

							<button
								@click="showRegisterPatient = true"
								class="w-full text-left px-3 py-2 text-sm text-blue-600 hover:text-blue-700 hover:bg-blue-50 rounded-md transition-colors"
							>
								+ Register New Patient
							</button>
						</div>
					</div>

					<!-- Select Doctor -->
					<div class="bg-white rounded-lg shadow p-6">
						<h2 class="text-lg font-semibold text-gray-900 mb-2">Select Doctor</h2>
						<p class="text-gray-600 mb-4">Choose a doctor for this appointment.</p>

						<select
							v-model="form.doctor"
							class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
							required
						>
							<option value="">Select a doctor</option>
							<option
								v-for="doctor in doctors"
								:key="doctor.id"
								:value="doctor.name"
							>
								{{ doctor.name }} - {{ doctor.specialty }}
							</option>
						</select>

						<!-- Selected Doctor Display -->
						<div
							v-if="selectedDoctor"
							class="mt-4 bg-gray-50 border border-gray-200 rounded-md p-3"
						>
							<div class="flex items-center">
								<img
									:src="selectedDoctor.avatar"
									:alt="selectedDoctor.name"
									class="h-10 w-10 rounded-full"
								/>
								<div class="ml-3">
									<p class="text-sm font-medium text-gray-900">
										{{ selectedDoctor.name }}
									</p>
									<p class="text-xs text-gray-500">
										{{ selectedDoctor.specialty }}
									</p>
									<p class="text-xs text-gray-500">
										{{ selectedDoctor.department }}
									</p>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, computed, watch } from 'vue'

const form = ref({
	appointmentType: '',
	date: '',
	time: '',
	duration: '30',
	reason: '',
	status: 'scheduled',
	doctor: '',
	additionalInfo: '',
})

const patientSearch = ref('')
const selectedPatient = ref(null)
const showRegisterPatient = ref(false)

const patients = ref([
	{
		id: 1,
		name: 'John Smith',
		email: 'john.smith@email.com',
		avatar: 'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
	},
	{
		id: 2,
		name: 'Emily Davis',
		email: 'emily.davis@email.com',
		avatar: 'https://images.unsplash.com/photo-1494790108755-2616c64c29d7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
	},
	{
		id: 3,
		name: 'Robert Wilson',
		email: 'robert.wilson@email.com',
		avatar: 'https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
	},
	{
		id: 4,
		name: 'Jessica Brown',
		email: 'jessica.brown@email.com',
		avatar: 'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
	},
	{
		id: 5,
		name: 'Michael Johnson',
		email: 'michael.johnson@email.com',
		avatar: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
	},
])

const doctors = ref([
	{
		id: 1,
		name: 'Dr. Sarah Johnson',
		specialty: 'General Medicine',
		department: 'Internal Medicine',
		avatar: 'https://images.unsplash.com/photo-1559839734-2b71ea197ec2?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
	},
	{
		id: 2,
		name: 'Dr. Michael Chen',
		specialty: 'Cardiology',
		department: 'Cardiology',
		avatar: 'https://images.unsplash.com/photo-1612349317150-e413f6a5b16d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
	},
	{
		id: 3,
		name: 'Dr. Lisa Patel',
		specialty: 'Pediatrics',
		department: 'Pediatrics',
		avatar: 'https://images.unsplash.com/photo-1594824475562-b1677fbe5f07?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
	},
	{
		id: 4,
		name: 'Dr. James Wilson',
		specialty: 'Dentistry',
		department: 'Dental',
		avatar: 'https://images.unsplash.com/photo-1582750433449-648ed127bb54?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
	},
	{
		id: 5,
		name: 'Dr. Emily Rodriguez',
		specialty: 'Radiology',
		department: 'Radiology',
		avatar: 'https://images.unsplash.com/photo-1527613426441-4da17471b66d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
	},
])

const timeSlots = [
	'08:00 AM',
	'08:30 AM',
	'09:00 AM',
	'09:30 AM',
	'10:00 AM',
	'10:30 AM',
	'11:00 AM',
	'11:30 AM',
	'12:00 PM',
	'12:30 PM',
	'01:00 PM',
	'01:30 PM',
	'02:00 PM',
	'02:30 PM',
	'03:00 PM',
	'03:30 PM',
	'04:00 PM',
	'04:30 PM',
	'05:00 PM',
	'05:30 PM',
	'06:00 PM',
]

const filteredPatients = computed(() => {
	if (!patientSearch.value) return []

	const query = patientSearch.value.toLowerCase()
	return patients.value.filter(
		(patient) =>
			patient.name.toLowerCase().includes(query) ||
			patient.email.toLowerCase().includes(query),
	)
})

const selectedDoctor = computed(() => {
	return doctors.value.find((doctor) => doctor.name === form.value.doctor)
})

const selectPatient = (patient) => {
	selectedPatient.value = patient
	patientSearch.value = ''
}

const clearPatientSelection = () => {
	selectedPatient.value = null
}

const searchPatients = () => {
	// Automatically show results when typing
}

const submitAppointment = () => {
	if (!selectedPatient.value) {
		alert('Please select a patient')
		return
	}

	const appointmentData = {
		...form.value,
		patient: selectedPatient.value,
		selectedDoctor: selectedDoctor.value,
	}

	console.log('Appointment Data:', appointmentData)
	alert('Appointment scheduled successfully!')

	// Reset form
	form.value = {
		appointmentType: '',
		date: '',
		time: '',
		duration: '30',
		reason: '',
		status: 'scheduled',
		doctor: '',
	}
	selectedPatient.value = null
}

const goBack = () => {
	// Navigate back to appointments list
	console.log('Going back to appointments list')
}

// Set default date to today
const today = new Date().toISOString().split('T')[0]
form.value.date = today
</script>
