import { useEffect, useState } from 'react'
import { Link, useNavigate, useSearchParams } from 'react-router-dom'
import { login, parseApiError, parseApiFieldErrors, register } from '../api/client'
import PasswordInput from '../components/PasswordInput'

const initialForm = {
  full_name: '',
  email: '',
  phone: '',
  iin: '',
  password: '',
  repeat_password: '',
  role: 'donor',
  personal_data_consent: false,
}

function fieldClassName(hasError) {
  return `w-full rounded-2xl border px-4 py-3 text-sm outline-none focus:border-teal-500 ${
    hasError ? 'border-red-300 focus:border-red-400' : 'border-sky-100'
  }`
}

function passwordFieldClassName(hasError) {
  return `w-full rounded-2xl border px-4 py-3 pr-12 text-sm outline-none focus:border-teal-500 ${
    hasError ? 'border-red-300 focus:border-red-400' : 'border-sky-100'
  }`
}

function FieldError({ message }) {
  if (!message) return null
  return <p className="text-xs text-red-600">{message}</p>
}

export default function Register() {
  const navigate = useNavigate()
  const [searchParams] = useSearchParams()
  const [form, setForm] = useState(initialForm)

  useEffect(() => {
    const role = searchParams.get('role')
    if (role === 'author' || role === 'donor') {
      setForm((prev) => ({ ...prev, role }))
    }
  }, [searchParams])
  const [error, setError] = useState('')
  const [fieldErrors, setFieldErrors] = useState({})
  const [loading, setLoading] = useState(false)

  function clearFieldError(field) {
    setFieldErrors((prev) => {
      if (!prev[field]) return prev
      const next = { ...prev }
      delete next[field]
      return next
    })
  }

  function updateField(field, value) {
    clearFieldError(field)
    setError('')
    setForm((prev) => ({ ...prev, [field]: value }))
  }

  async function handleSubmit(event) {
    event.preventDefault()
    setError('')
    setFieldErrors({})
    if (!form.personal_data_consent) {
      setError('Необходимо согласие на обработку персональных данных.')
      return
    }
    if (!/^\d{12}$/.test(form.iin)) {
      setFieldErrors({ iin: 'ИИН должен содержать ровно 12 цифр.' })
      return
    }
    setLoading(true)
    try {
      await register({
        full_name: form.full_name,
        email: form.email,
        phone: form.phone,
        iin: form.iin,
        password: form.password,
        repeat_password: form.repeat_password,
        role: form.role,
      })
      await login(form.email, form.password)
      navigate(form.role === 'author' ? '/author' : '/')
    } catch (err) {
      if (!err.data && !err.status) {
        setError('Сервер недоступен. Запустите backend: python manage.py runserver')
        return
      }
      const fields = parseApiFieldErrors(err.data)
      setFieldErrors(fields)
      setError(
        fields._form
          || (Object.keys(fields).filter((key) => key !== '_form').length === 0
            ? parseApiError(err.data, 'Не удалось зарегистрироваться.')
            : '')
      )
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="mx-auto max-w-lg px-4 py-16">
      <form onSubmit={handleSubmit} className="space-y-4 rounded-3xl bg-white p-8 shadow-md">
        <p className="text-sm font-semibold text-teal-600">е-Көмек</p>
        <p className="text-xs text-slate-500">Сенімді көмек</p>
        <h1 className="text-2xl font-semibold text-slate-800">Регистрация</h1>
        <div className="space-y-1">
          <input
            type="text"
            placeholder="ФИО"
            value={form.full_name}
            onChange={(e) => updateField('full_name', e.target.value)}
            required
            className={fieldClassName(fieldErrors.full_name)}
          />
          <FieldError message={fieldErrors.full_name} />
        </div>
        <div className="space-y-1">
          <input
            type="email"
            placeholder="Email"
            value={form.email}
            onChange={(e) => updateField('email', e.target.value)}
            required
            className={fieldClassName(fieldErrors.email)}
          />
          <FieldError message={fieldErrors.email} />
        </div>
        <div className="space-y-1">
          <input
            type="text"
            placeholder="Телефон"
            value={form.phone}
            onChange={(e) => updateField('phone', e.target.value)}
            className={fieldClassName(fieldErrors.phone)}
          />
          <FieldError message={fieldErrors.phone} />
        </div>
        <div className="space-y-1">
          <input
            type="text"
            placeholder="ИИН (12 цифр)"
            value={form.iin}
            onChange={(e) => updateField('iin', e.target.value.replace(/\D/g, '').slice(0, 12))}
            required
            pattern="\d{12}"
            maxLength={12}
            className={fieldClassName(fieldErrors.iin)}
          />
          <FieldError message={fieldErrors.iin} />
        </div>
        <div className="space-y-1">
          <select
            value={form.role}
            onChange={(e) => updateField('role', e.target.value)}
            className={fieldClassName(fieldErrors.role)}
          >
            <option value="donor">Донор</option>
            <option value="author">Автор сбора</option>
          </select>
          <FieldError message={fieldErrors.role} />
        </div>
        <div className="space-y-1">
          <PasswordInput
            placeholder="Пароль"
            value={form.password}
            onChange={(e) => updateField('password', e.target.value)}
            required
            minLength={8}
            className={passwordFieldClassName(fieldErrors.password)}
          />
          <FieldError message={fieldErrors.password} />
        </div>
        <p className="text-xs text-slate-500">Минимум 8 символов</p>
        <div className="space-y-1">
          <PasswordInput
            placeholder="Повторите пароль"
            value={form.repeat_password}
            onChange={(e) => updateField('repeat_password', e.target.value)}
            required
            className={passwordFieldClassName(fieldErrors.repeat_password)}
          />
          <FieldError message={fieldErrors.repeat_password} />
        </div>
        <label className="flex items-start gap-3 text-sm text-slate-600">
          <input
            type="checkbox"
            checked={form.personal_data_consent}
            onChange={(e) => updateField('personal_data_consent', e.target.checked)}
            className="mt-1"
          />
          <span>Согласен(на) на обработку персональных данных</span>
        </label>
        {error && <p className="text-sm text-red-600">{error}</p>}
        <button
          type="submit"
          disabled={loading}
          className="w-full rounded-2xl bg-teal-500 px-6 py-4 font-semibold text-white hover:bg-teal-600 disabled:opacity-60"
        >
          {loading ? 'Регистрация...' : 'Зарегистрироваться'}
        </button>
        <p className="text-center text-sm text-slate-600">
          Уже есть аккаунт?{' '}
          <Link to="/login" className="font-medium text-teal-600 hover:underline">
            Войти
          </Link>
        </p>
      </form>
    </div>
  )
}
